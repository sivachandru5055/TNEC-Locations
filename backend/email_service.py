"""
Email OTP Service
-----------------
Handles OTP generation and email sending via Gmail SMTP.
"""
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from database import settings


def generate_otp() -> str:
    """Generate a random 6-digit OTP."""
    return str(random.randint(100000, 999999))


def send_otp_email(to_email: str, name: str, otp: str) -> bool:
    """Send OTP verification email to new user."""
    subject = "OTP Verification - TNECL"
    display_name = name if name else "User"

    html_body = f"""
    <html>
    <body style="font-family: Arial, sans-serif; background-color: #0a0f1c; color: #e0e6ed; padding: 20px;">
        <div style="max-width: 480px; margin: auto; background: #141b2d; border-radius: 12px; padding: 32px; border: 1px solid #1e293b;">
            <h2 style="color: #60a5fa; margin-top: 0;">TNECL Account Verification</h2>
            <p>Dear <strong>{display_name}</strong>,</p>
            <p>Thank you for registering with TNECL. Your OTP for account verification is:</p>
            <div style="text-align: center; margin: 24px 0;">
                <span style="display: inline-block; font-size: 32px; font-weight: bold; letter-spacing: 8px; color: #60a5fa; background: #1e293b; padding: 16px 32px; border-radius: 8px;">{otp}</span>
            </div>
            <p style="color: #94a3b8; font-size: 14px;">This OTP is valid for <strong>10 minutes</strong>. Do not share it with anyone.</p>
            <hr style="border: none; border-top: 1px solid #1e293b; margin: 24px 0;">
            <p style="color: #64748b; font-size: 12px;">If you did not request this, please ignore this email.</p>
        </div>
    </body>
    </html>
    """
    return _send_email(to_email, subject, html_body)


def send_resend_otp_email(to_email: str, otp: str) -> bool:
    """Send a resent OTP email."""
    subject = "OTP Verification (Resend) - TNECL"

    html_body = f"""
    <html>
    <body style="font-family: Arial, sans-serif; background-color: #0a0f1c; color: #e0e6ed; padding: 20px;">
        <div style="max-width: 480px; margin: auto; background: #141b2d; border-radius: 12px; padding: 32px; border: 1px solid #1e293b;">
            <h2 style="color: #60a5fa; margin-top: 0;">New OTP Code</h2>
            <p>Dear User,</p>
            <p>Your new OTP for account verification is:</p>
            <div style="text-align: center; margin: 24px 0;">
                <span style="display: inline-block; font-size: 32px; font-weight: bold; letter-spacing: 8px; color: #60a5fa; background: #1e293b; padding: 16px 32px; border-radius: 8px;">{otp}</span>
            </div>
            <p style="color: #94a3b8; font-size: 14px;">This OTP is valid for <strong>10 minutes</strong>. Do not share it with anyone.</p>
            <hr style="border: none; border-top: 1px solid #1e293b; margin: 24px 0;">
            <p style="color: #64748b; font-size: 12px;">If you did not request this, please ignore this email.</p>
        </div>
    </body>
    </html>
    """
    return _send_email(to_email, subject, html_body)


def _send_email(to_email: str, subject: str, html_body: str) -> bool:
    """Internal helper to send an HTML email via Gmail SMTP."""
    sender_email = settings.smtp_email
    sender_password = settings.smtp_password

    if not sender_email or not sender_password:
        print("WARNING: SMTP credentials not configured in .env")
        return False

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = f"TNECL <{sender_email}>"
    msg["To"] = to_email
    msg.attach(MIMEText(html_body, "html"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, msg.as_string())
        print(f"OTP email sent to {to_email}")
        return True
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")
        return False
