from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from jose import JWTError, jwt
from database import db, settings
from models import College, User, UserCreate, Token, TokenData, OTPVerify, ResendOTP, LoginRequest
from auth import verify_password, get_password_hash, create_access_token
from email_service import generate_otp, send_otp_email, send_resend_otp_email
from typing import List
from datetime import datetime, timedelta

app = FastAPI(title="TNECL API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user = await db["users"].find_one({"email": token_data.email})
    if user is None:
        raise credentials_exception
    return User(**user)

# ─── Registration with OTP ───────────────────────────────────────────

@app.post("/register")
async def register(user: UserCreate):
    existing_user = await db["users"].find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    if len(user.password.encode('utf-8')) > 72:
        raise HTTPException(status_code=400, detail="Password must not exceed 72 bytes")

    hashed_password = get_password_hash(user.password)
    user_dict = user.model_dump()
    user_dict["hashed_password"] = hashed_password
    user_dict["is_verified"] = False
    del user_dict["password"]

    await db["users"].insert_one(user_dict)

    # Generate and store OTP
    otp = generate_otp()
    await db["otps"].delete_many({"email": user.email})
    await db["otps"].insert_one({
        "email": user.email,
        "otp": otp,
        "created_at": datetime.utcnow(),
        "expires_at": datetime.utcnow() + timedelta(minutes=10)
    })

    # Send OTP email
    email_sent = send_otp_email(user.email, user.name or "User", otp)

    if not email_sent:
        raise HTTPException(status_code=500, detail="Failed to send OTP email. Please check SMTP configuration.")

    return {"message": "Registration successful! OTP has been sent to your email.", "email": user.email, "verified": False}

# ─── Verify OTP ──────────────────────────────────────────────────────

@app.post("/verify-otp")
async def verify_otp(data: OTPVerify):
    # Find OTP record
    otp_record = await db["otps"].find_one({"email": data.email})
    if not otp_record:
        raise HTTPException(status_code=400, detail="No OTP found. Please register or resend OTP.")

    # Check expiry
    if datetime.utcnow() > otp_record["expires_at"]:
        await db["otps"].delete_many({"email": data.email})
        raise HTTPException(status_code=400, detail="OTP has expired. Please request a new one.")

    # Verify OTP
    if otp_record["otp"] != data.otp:
        raise HTTPException(status_code=400, detail="Invalid OTP. Please try again.")

    # Mark user as verified
    await db["users"].update_one(
        {"email": data.email},
        {"$set": {"is_verified": True}}
    )

    # Clean up OTP
    await db["otps"].delete_many({"email": data.email})

    return {"message": "Email verified successfully! You can now login."}

# ─── Resend OTP ──────────────────────────────────────────────────────

@app.post("/resend-otp")
async def resend_otp(data: ResendOTP):
    user = await db["users"].find_one({"email": data.email})
    if not user:
        raise HTTPException(status_code=404, detail="Email not found. Please register first.")

    if user.get("is_verified"):
        raise HTTPException(status_code=400, detail="Email is already verified.")

    # Generate new OTP
    otp = generate_otp()
    await db["otps"].delete_many({"email": data.email})
    await db["otps"].insert_one({
        "email": data.email,
        "otp": otp,
        "created_at": datetime.utcnow(),
        "expires_at": datetime.utcnow() + timedelta(minutes=10)
    })

    send_resend_otp_email(data.email, otp)

    return {"message": "New OTP sent to your email."}

# ─── Login Step 1: Validate credentials & send OTP ───────────────────

@app.post("/login-request")
async def login_request(data: LoginRequest):
    user = await db["users"].find_one({"email": data.email})
    if not user or len(data.password.encode('utf-8')) > 72 or not verify_password(data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )

    # Generate and store login OTP
    otp = generate_otp()
    await db["otps"].delete_many({"email": data.email})
    await db["otps"].insert_one({
        "email": data.email,
        "otp": otp,
        "created_at": datetime.utcnow(),
        "expires_at": datetime.utcnow() + timedelta(minutes=10)
    })

    # Send OTP email
    email_sent = send_otp_email(data.email, user.get("name", "User"), otp)

    if not email_sent:
        raise HTTPException(status_code=500, detail="Failed to send OTP email. Please check SMTP configuration.")

    return {"message": "OTP has been sent to your email.", "email": data.email}

# ─── Login Step 2: Verify OTP & return JWT ────────────────────────────

@app.post("/login-verify", response_model=Token)
async def login_verify(data: OTPVerify):
    # Find OTP record
    otp_record = await db["otps"].find_one({"email": data.email})
    if not otp_record:
        raise HTTPException(status_code=400, detail="No OTP found. Please try logging in again.")

    if datetime.utcnow() > otp_record["expires_at"]:
        await db["otps"].delete_many({"email": data.email})
        raise HTTPException(status_code=400, detail="OTP expired. Please try again.")

    if otp_record["otp"] != data.otp:
        raise HTTPException(status_code=400, detail="Invalid OTP.")

    # Clean up OTP
    await db["otps"].delete_many({"email": data.email})

    # Also mark user as verified if not already
    await db["users"].update_one({"email": data.email}, {"$set": {"is_verified": True}})

    # Generate JWT
    user = await db["users"].find_one({"email": data.email})
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": user["email"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# ─── Legacy token endpoint (for OAuth2 compatibility) ─────────────────

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await db["users"].find_one({"email": form_data.username})
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": user["email"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# ─── College endpoints ────────────────────────────────────────────────

@app.get("/colleges", response_model=List[College], response_model_by_alias=True)
async def read_colleges(skip: int = 0, limit: int = 500):
    colleges = await db["colleges"].find().skip(skip).limit(limit).to_list(limit)
    for college in colleges:
        college["_id"] = str(college["_id"])
        if not college.get("zone") and college.get("code"):
            try:
                college["zone"] = int(str(college["code"])[0])
            except (ValueError, IndexError):
                college["zone"] = 0
    return [College(**college) for college in colleges]

@app.get("/colleges/{college_id}", response_model=College, response_model_by_alias=True)
async def read_college(college_id: str):
    from bson import ObjectId
    from bson.errors import InvalidId

    try:
        obj_id = ObjectId(college_id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid college ID format")

    college = await db["colleges"].find_one({"_id": obj_id})
    if college is None:
        raise HTTPException(status_code=404, detail="College not found")
    college["_id"] = str(college["_id"])
    return College(**college)

@app.post("/admin/sync-fees")
async def sync_fees(current_user: User = Depends(get_current_user)):
    from scraper import update_college_fees
    count = await update_college_fees()
    return {"message": f"Successfully updated fees for {count} colleges"}
