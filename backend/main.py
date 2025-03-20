from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
import httpx
from app.services.firebase_service import firebase_admin
from app.routers import crop_router, auth_router
from dotenv import load_dotenv

load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

if not WEATHER_API_KEY:
    raise ValueError("WEATHER_API_KEY is not set. Please check your environment variables.")

app = FastAPI(title="Crop Recommendation API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"

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

@app.get("/weather/")
async def get_weather():
    location = "Parang, Calapan City, Oriental Mindoro"  # Fixed location

    params = {
        "key": WEATHER_API_KEY,
        "q": location,  # City name
        "aqi": "no"  # Disable Air Quality Index
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(WEATHER_API_URL, params=params)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch weather data")

    weather_data = response.json()

    # Extract necessary weather data
    wind_speed_kph = weather_data["current"]["wind_kph"]
    wind_speed_ms = round(wind_speed_kph / 3.6, 2)  # Convert km/h to m/s

    weather_info = {
        "location": weather_data["location"]["name"],
        "region": weather_data["location"]["region"],
        "country": weather_data["location"]["country"],
        "temperature_c": weather_data["current"]["temp_c"],  # Temperature in °C
        "temperature_f": weather_data["current"]["temp_f"],  # Temperature in °F
        "humidity": weather_data["current"]["humidity"],  # Humidity in %
        "wind_speed_kph": wind_speed_kph,  # Wind speed in km/h
        "wind_speed_ms": wind_speed_ms,  # Wind speed in m/s (converted)
        "pressure_hpa": weather_data["current"]["pressure_mb"],  # Pressure in hPa
        "cloud_cover_percent": weather_data["current"]["cloud"],  # Cloud cover in %
        "weather_condition": weather_data["current"]["condition"]["text"],  # Weather condition (e.g., "Clear")
        "rain_mm": weather_data["current"].get("precip_mm", 0),  # Rain in mm (if available)
    }

    return weather_info
