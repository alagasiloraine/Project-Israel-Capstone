from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel, EmailStr  
from datetime import datetime, timedelta
from app.services.firebase_service import auth, db, send_verification_email, send_login_notification, firestore, forgot_password_verification_email
import random
import pytz

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

        # Set expiration time for the verification code (10 minutes from now)
        expiration_time = datetime.utcnow() + timedelta(minutes=10)

        # Save user in Firestore using UID, including verification code and expiration time
        user_data = {
            "firstName": user.firstName,
            "lastName": user.lastName,
            "email": user.email,
            "createdAt": datetime.utcnow().isoformat(),
            "verified": False,
            "verificationCode": verification_code,
            "verificationCodeExpiration": expiration_time.isoformat()  # Store expiration time
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

    # Check if the code has expired (if expiration time is present)
    expiration_time = user_info.get("verificationCodeExpiration")
    if expiration_time:
        expiration_time = datetime.fromisoformat(expiration_time)
        if datetime.utcnow() > expiration_time:
            raise HTTPException(status_code=400, detail="Verification code has expired. Request a new one.")

    # Generate a new code and update Firestore
    new_verification_code = generate_verification_code(6)
    new_expiration_time = datetime.utcnow() + timedelta(minutes=10)  # 10 minutes expiration
    user_ref.update({
        "verificationCode": new_verification_code,
        "verificationCodeExpiration": new_expiration_time.isoformat()  # Update expiration time
    })

    # Resend the email
    send_verification_email(user_info["email"], new_verification_code)
    
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

    # Update user as verified and remove the verification code
    user_ref.update({
        "verified": True,
        "verificationCode": firestore.DELETE_FIELD  # This removes the field
    })

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

        send_login_notification(data.email)

        return {
            "message": "Login successful",
            "token": res_data["idToken"],
            "userId": res_data["localId"]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/google-register")
async def google_register(request: Request):
    try:
        # Parse the JSON body of the request
        body = await request.json()
        idToken = body.get("idToken")

        if not idToken:
            raise HTTPException(status_code=422, detail="idToken is required")

        # 🔹 Verify the Firebase ID Token
        decoded_token = auth.verify_id_token(idToken)
        uid = decoded_token.get("uid")
        email = decoded_token.get("email")
        name = decoded_token.get("name")

        if not uid or not email:
            raise HTTPException(status_code=400, detail="Invalid Google user data")

        # 🔹 Check if user already exists
        user_ref = firestore.client().collection("users").document(uid)
        user_doc = user_ref.get()

        if user_doc.exists:
            return {"message": "User already registered", "userId": uid}

        # 🔹 Register new user in Firestore
        user_data = {
            "uid": uid,
            "name": name,
            "email": email,
            "createdAt": datetime.utcnow().isoformat(),
            "verified": True  # Google users are automatically verified
        }
        user_ref.set(user_data)

        send_login_notification(email)

        return {"message": "User registered successfully", "userId": uid}

    except Exception as e:
        print(f"❌ Firebase Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Google registration failed")
    

@router.post("/google-login")
async def google_login(request: Request):
    try:
        # Parse the JSON body of the request
        body = await request.json()
        idToken = body.get("idToken")

        if not idToken:
            raise HTTPException(status_code=422, detail="idToken is required")

        # 🔹 Verify the Firebase ID Token
        decoded_token = auth.verify_id_token(idToken)
        uid = decoded_token.get("uid")
        email = decoded_token.get("email")
        name = decoded_token.get("name")

        if not uid or not email:
            raise HTTPException(status_code=400, detail="Invalid Google user data")

        # 🔹 Check if user exists
        user_ref = firestore.client().collection("users").document(uid)
        user_doc = user_ref.get()

        if not user_doc.exists:
            # If user doesn't exist in Firestore, register them
            user_data = {
                "uid": uid,
                "name": name,
                "email": email,
                "createdAt": firestore.SERVER_TIMESTAMP,
                "verified": True  # Google users are automatically verified
            }
            user_ref.set(user_data)

        # 🔹 Send login notification email
        send_login_notification(email)

        return {"message": "Login successful", "userId": uid}

    except Exception as e:
        print(f"❌ Firebase Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Google login failed")
    

# Request model for forgot password
class ForgotPasswordRequest(BaseModel):
    email: str

@router.post("/forgot-password")
async def forgot_password(request: ForgotPasswordRequest):
    try:
        # 🔹 Check if user exists
        try:
            user = auth.get_user_by_email(request.email)
        except auth.UserNotFoundError:
            raise HTTPException(status_code=400, detail="User not found")

        # 🔹 Generate a random 6-digit verification code
        verification_code = generate_verification_code(6)

        # 🔹 Set explicit expiration time (10 minutes from now)
        expiration_time = datetime.utcnow().replace(tzinfo=pytz.UTC) + timedelta(minutes=10)

        # 🔹 Store the code in Firestore
        db.collection("password_reset_codes").document(request.email).set({
            "code": verification_code,
            "expires_at": expiration_time.strftime("%Y-%m-%d %H:%M:%S.%f%z")  # Store as string to avoid Firestore timezone issues
        })

        # 🔹 Send the code via email
        forgot_password_verification_email(request.email, verification_code)

        return {"message": "Verification code sent to your email"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
class VerifyCodeRequest(BaseModel):
    email: str
    code: str
# ✅ Step 2: Verify the 6-digit code
@router.post("/verify-code")
async def verify_code(request: VerifyCodeRequest):
    try:
        # Fetch the document from Firestore
        doc_ref = db.collection("password_reset_codes").document(request.email)
        doc = doc_ref.get()

        if not doc.exists:
            raise HTTPException(status_code=400, detail="No verification code found. Request a new one.")

        stored_data = doc.to_dict()
        stored_code = stored_data.get("code")
        expires_at = stored_data.get("expires_at")  # Get expiration timestamp

        # Log the stored and entered codes for debugging
        print(f"Stored code: {stored_code}")
        print(f"Entered code: {request.code}")

        # 🔹 Convert Firestore timestamp to Python datetime
        if expires_at:
            if isinstance(expires_at, str):  # If the value is a string, parse it as a datetime
                expires_at_dt = datetime.fromisoformat(expires_at)
            else:
                expires_at_dt = expires_at.to_pydatetime()  # Convert Firestore timestamp to Python datetime
            
            current_time = datetime.utcnow().replace(tzinfo=pytz.UTC)  # Get current time with timezone info

            # 🔹 Check if the code is expired
            if current_time > expires_at_dt:
                raise HTTPException(status_code=400, detail="Verification code expired. Request a new one.")

        # 🔹 Validate code
        if stored_code != request.code:
            raise HTTPException(status_code=400, detail="Invalid verification code. Please check and try again.")

        return {"message": "Verification successful"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

class ResetPasswordRequest(BaseModel):
    email: str
    new_password: str

@router.post("/reset-password")
async def reset_password(request: ResetPasswordRequest):
    try:
        # Get the password reset code document
        doc_ref = db.collection("password_reset_codes").document(request.email)
        doc = doc_ref.get()

        if not doc.exists:
            raise HTTPException(status_code=400, detail="No verification code found. Request a new one.")

        # Update the password in Firebase Authentication
        try:
            user = auth.get_user_by_email(request.email)
            auth.update_user(user.uid, password=request.new_password)
        except auth.UserNotFoundError:
            raise HTTPException(status_code=404, detail="User not found in Firebase Authentication.")

        return {"message": "Password successfully updated."}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))