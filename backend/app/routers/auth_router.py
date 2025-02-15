from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr  
from datetime import datetime
from app.services.firebase_service import auth, db, send_verification_email
import random

router = APIRouter()

class RegisterUserRequest(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    password: str
    acceptTerms: bool

# ✅ Generate a 6-digit numeric code
def generate_verification_code(length=6):
    return "".join(str(random.randint(0, 9)) for _ in range(length))

@router.post("/register")
async def register_user(user: RegisterUserRequest):
    print("🚀 Incoming Request Data:", user.dict())  # Debugging

    # Check if Firestore is available
    if not db:
        raise HTTPException(status_code=500, detail="Firebase Firestore not initialized")

    try:
        # Ensure terms are accepted
        if not user.acceptTerms:
            raise HTTPException(status_code=400, detail="You must accept the terms and conditions.")

        # Create Firebase Auth user
        auth_user = auth.create_user(email=user.email, password=user.password)
        uid = auth_user.uid  # Get Firebase UID

        # Generate verification code (6-digit numeric)
        verification_code = generate_verification_code(6)

        # Save user in Firestore using UID
        user_data = {
            "firstName": user.firstName,
            "lastName": user.lastName,
            "email": user.email,
            "createdAt": datetime.utcnow().isoformat(),
            "verified": False,
            "verificationCode": verification_code
        }

        db.collection("users").document(uid).set(user_data)  

        # Send verification email
        send_verification_email(user.email, verification_code)

        return {"message": "User registered successfully. Check your email for verification.", "userId": uid}

    except auth.EmailAlreadyExistsError:
        print("❌ Error: Email already exists")
        raise HTTPException(status_code=400, detail="Email already exists.")

    except Exception as e:
        print(f"❌ Unexpected Error: {str(e)}")  # Log error for debugging
        raise HTTPException(status_code=500, detail=str(e))
    

class ResendCodeRequest(BaseModel):
    uid: str

@router.post("/resend-code")
async def resend_code(data: ResendCodeRequest):
    print("📩 Received Resend Code Request:", data.dict())  # Debugging
    uid = data.uid
    if not uid:
        raise HTTPException(status_code=400, detail="UID is required.")
    
    user_ref = db.collection("users").document(uid)
    user_data = user_ref.get()

    if not user_data.exists:
        raise HTTPException(status_code=404, detail="User not found")

    user_info = user_data.to_dict()

    if user_info["verified"]:
        return {"message": "User is already verified"}

    # Generate a new code and update Firestore
    new_verification_code = generate_verification_code(6)
    user_ref.update({"verificationCode": new_verification_code})

    # Resend the email
    send_verification_email(user_info["email"], new_verification_code)
    
    # Your resend code logic...
    return {"message": "New verification code sent"}

    
class VerifyEmailRequest(BaseModel):
    uid: str
    code: str

@router.post("/verify-email")
async def verify_email(data: VerifyEmailRequest):
    uid = data.uid
    code = data.code

    user_ref = db.collection("users").document(uid)
    user_data = user_ref.get()

    if not user_data.exists:
        raise HTTPException(status_code=404, detail="User not found")

    user_info = user_data.to_dict()

    if user_info["verified"]:
        return {"message": "User is already verified"}

    if user_info["verificationCode"] != code:
        raise HTTPException(status_code=400, detail="Invalid verification code")

    # Update user as verified
    user_ref.update({"verified": True})

    return {"message": "Email successfully verified"}

from dotenv import load_dotenv
import os

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
async def login_user(data: LoginRequest):
    try:
        # Authenticate the user with Firebase
        user = auth.get_user_by_email(data.email)
        if not user:
            raise HTTPException(status_code=400, detail="Invalid email or password")

        # Sign in the user using Firebase's REST API (since Firebase Admin SDK does not support password authentication)
        import requests
        FIREBASE_API_KEY = os.getenv("API_KEY")  # Replace with your Firebase API key
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_API_KEY}"
        payload = {
            "email": data.email,
            "password": data.password,
            "returnSecureToken": True
        }
        headers = {"Content-Type": "application/json"}
        
        response = requests.post(url, json=payload, headers=headers)
        res_data = response.json()

        if "error" in res_data:
            raise HTTPException(status_code=400, detail=res_data["error"]["message"])

        return {
            "message": "Login successful",
            "token": res_data["idToken"],
            "userId": res_data["localId"]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))