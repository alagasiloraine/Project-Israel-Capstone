import firebase_admin
from firebase_admin import credentials, auth, firestore
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load Firebase credentials dynamically
FIREBASE_CREDENTIALS = os.getenv("FIREBASE_CREDENTIALS")
if not FIREBASE_CREDENTIALS:
    raise ValueError("Firebase credentials not found. Set FIREBASE_CREDENTIALS in .env")

# Initialize Firebase App (Singleton)
if not firebase_admin._apps:  # Prevent re-initialization
    cred = credentials.Certificate(FIREBASE_CREDENTIALS)
    firebase_admin.initialize_app(cred)

# Firestore client
db = firestore.client()

# Function to generate verification code
import random
import string

def generate_verification_code(length=6):
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=length))

# Function to send verification email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587  # Change to 587
SMTP_USERNAME = os.getenv("SMTP_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SENDER_EMAIL = SMTP_USERNAME

print("SMTP Email:", SMTP_USERNAME)
print("SMTP Password:", "Loaded" if SMTP_PASSWORD else "Not Loaded")

def send_verification_email(email, verification_code):
    subject = "Verify Your Email - Crop Recommendation System"
    body = f"""
    <html>
        <body>
            <h2>Email Verification</h2>
            <p>Hello,</p>
            <p>Thank you for registering. Please use the following verification code to verify your email:</p>
            <h3>{verification_code}</h3>
            <p>If you did not request this, please ignore this email.</p>
            <p>Best Regards,<br>Crop Recommendation Team</p>
        </body>
    </html>
    """

    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))

    try:
        # Use Port 587 with starttls()
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(SENDER_EMAIL, email, msg.as_string())

        print(f"✅ Verification email sent to {email}")

    except Exception as e:
        print(f"❌ Failed to send email: {e}")
