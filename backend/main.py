from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from app.services.firebase_service import firebase_admin
from app.routers import crop_router, auth_router

app = FastAPI(title="Crop Recommendation API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(crop_router.router, prefix="/api/crop", tags=["crop"])
app.include_router(auth_router.router, prefix="/api/auth", tags=["auth"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Crop Recommendation API"}

@app.get("/firebase-test")
async def firebase_test():
    if firebase_admin:
        return {"message": "Firebase is initialized successfully"}
    return {"error": "Firebase initialization failed"}
