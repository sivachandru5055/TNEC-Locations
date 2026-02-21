from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional, List
from datetime import datetime

class CollegeBase(BaseModel):
    name: str
    code: Optional[str] = None
    website: Optional[str] = None
    location: str
    type: str  # Government, Private, etc.
    affiliated_to: str
    fees_btech: float
    fees_mtech: float
    avg_package: float
    latitude: float
    longitude: float
    location_url: Optional[str] = None
    zone: Optional[int] = None

class CollegeCreate(CollegeBase):
    pass

class College(CollegeBase):
    model_config = ConfigDict(populate_by_name=True)
    id: str = Field(alias="_id")

class UserBase(BaseModel):
    email: EmailStr
    name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    model_config = ConfigDict(populate_by_name=True)
    id: str = Field(alias="_id")
    disabled: Optional[bool] = False
    is_verified: Optional[bool] = False

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

# OTP models
class OTPVerify(BaseModel):
    email: EmailStr
    otp: str

class ResendOTP(BaseModel):
    email: EmailStr

class LoginRequest(BaseModel):
    email: EmailStr
    password: str
