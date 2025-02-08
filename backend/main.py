from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import crop_router

app = FastAPI(title="Crop Recommendation API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(crop_router.router, prefix="/api/crop", tags=["crop"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Crop Recommendation API"}
