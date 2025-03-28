# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# import os
# import httpx
# from app.services.firebase_service import firebase_admin
# from app.routers import crop_router, auth_router, forecast_router
# from dotenv import load_dotenv

# load_dotenv()
# WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# if not WEATHER_API_KEY:
#     raise ValueError("WEATHER_API_KEY is not set. Please check your environment variables.")

# app = FastAPI(title="Crop Recommendation API")

# # Configure CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"

# # Include routers
# app.include_router(crop_router.router, prefix="/api/crop", tags=["crop"])
# app.include_router(auth_router.router, prefix="/api/auth", tags=["auth"])
# app.include_router(forecast_router.router, prefix="/api/weather", tags=["weather"])

# @app.get("/")
# async def root():
#     return {"message": "Welcome to the Crop Recommendation API"}

# @app.get("/firebase-test")
# async def firebase_test():
#     if firebase_admin:
#         return {"message": "Firebase is initialized successfully"}
#     return {"error": "Firebase initialization failed"}

# @app.get("/weather/")
# async def get_weather():
#     location = "Parang, Calapan City, Oriental Mindoro"  # Fixed location

#     params = {
#         "key": WEATHER_API_KEY,
#         "q": location,  # City name
#         "aqi": "no"  # Disable Air Quality Index
#     }

#     async with httpx.AsyncClient() as client:
#         response = await client.get(WEATHER_API_URL, params=params)

#     if response.status_code != 200:
#         raise HTTPException(status_code=response.status_code, detail="Failed to fetch weather data")

#     weather_data = response.json()

#     # Extract necessary weather data
#     wind_speed_kph = weather_data["current"]["wind_kph"]
#     wind_speed_ms = round(wind_speed_kph / 3.6, 2)  # Convert km/h to m/s

#     weather_info = {
#         "location": weather_data["location"]["name"],
#         "region": weather_data["location"]["region"],
#         "country": weather_data["location"]["country"],
#         "temperature_c": weather_data["current"]["temp_c"],  # Temperature in °C
#         "temperature_f": weather_data["current"]["temp_f"],  # Temperature in °F
#         "humidity": weather_data["current"]["humidity"],  # Humidity in %
#         "wind_speed_kph": wind_speed_kph,  # Wind speed in km/h
#         "wind_speed_ms": wind_speed_ms,  # Wind speed in m/s (converted)
#         "pressure_hpa": weather_data["current"]["pressure_mb"],  # Pressure in hPa
#         "cloud_cover_percent": weather_data["current"]["cloud"],  # Cloud cover in %
#         "weather_condition": weather_data["current"]["condition"]["text"],  # Weather condition (e.g., "Clear")
#         "rain_mm": weather_data["current"].get("precip_mm", 0),  # Rain in mm (if available)
#         "uv": weather_data["current"].get("uv", 0), # UV
#     }

#     return weather_info



from fastapi import FastAPI, HTTPException, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import os
import httpx
import asyncio
import serial
import json
import logging

from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler

from app.services.firebase_service import firebase_admin
from app.routers import crop_router, auth_router, forecast_router, sensor_data, npk_router
from app.ml.weather_ml.forecast.forecast import main as run_forecast

# ======== ENV & LOG SETUP ===========
load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
if not WEATHER_API_KEY:
    raise ValueError("WEATHER_API_KEY is not set. Please check your .env file.")

logging.basicConfig(
    filename="forecast_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ======== FASTAPI APP SETUP =========
app = FastAPI(title="Crop Recommendation API")

# ======== CORS CONFIG =========
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ======== ROUTERS =========
app.include_router(crop_router.router, prefix="/api/crop", tags=["crop"])
app.include_router(auth_router.router, prefix="/api/auth", tags=["auth"])
app.include_router(forecast_router.router, prefix="/api/weather", tags=["weather"])
# app.include_router(npk_router.router, prefix="/api/npk", tags=["npk"])
app.include_router(sensor_data.router)

# ======== MIDDLEWARE FOR WS =========
@app.middleware("http")
async def allow_websocket_cors(request, call_next):
    if request.scope["type"] == "websocket":
        return await npk_router.websocket_endpoint(request)
    return await call_next(request)

# ======== ROUTES =========
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
    latitude = 13.405327079018555
    longitude = 121.21506521885358
    coordinates = f"{latitude},{longitude}"

    params = {
        "key": WEATHER_API_KEY,
        "q": coordinates,
        "aqi": "no"
    }

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get("http://api.weatherapi.com/v1/current.json", params=params)
            response.raise_for_status()
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Weather API error: {e}")

    weather_data = response.json()
    wind_speed_kph = weather_data["current"]["wind_kph"]
    wind_speed_ms = round(wind_speed_kph / 3.6, 2)

    return {
        "location": weather_data["location"]["name"],
        "region": weather_data["location"]["region"],
        "country": weather_data["location"]["country"],
        "temperature_c": weather_data["current"]["temp_c"],
        "temperature_f": weather_data["current"]["temp_f"],
        "humidity": weather_data["current"]["humidity"],
        "wind_speed_kph": wind_speed_kph,
        "wind_speed_ms": wind_speed_ms,
        "pressure_hpa": weather_data["current"]["pressure_mb"],
        "cloud_cover_percent": weather_data["current"]["cloud"],
        "weather_condition": weather_data["current"]["condition"]["text"],
        "rain_mm": weather_data["current"].get("precip_mm", 0),
        "uv": weather_data["current"].get("uv", 0),
        "last_updated": weather_data["current"].get("last_updated")
    }

# ======== SERIAL READER =========
SERIAL_PORT = 'COM4'
BAUD_RATE = 9600

async def read_serial_loop():
    await asyncio.sleep(2)  # Allow FastAPI to fully start
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        print(f"✅ Connected to Arduino on {SERIAL_PORT}")
        
        while True:
            try:
                line = ser.readline().decode('utf-8').strip()
                if line:
                    try:
                        data = json.loads(line)
                        await sensor_data.forward_sensor_data(data)
                    except json.JSONDecodeError:
                        print("⚠️ Invalid JSON:", line)
            except Exception as e:
                print("❌ Error reading serial:", e)
            await asyncio.sleep(0.1)

    except Exception as e:
        print("❌ Could not open serial port:", e)

# ======== STARTUP EVENTS =========
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(read_serial_loop())

    scheduler = BackgroundScheduler()
    scheduler.add_job(run_forecast_task, 'interval', days=1)
    scheduler.start()
    print("📅 Forecast scheduler started (daily)")
    logging.info("📅 Forecast scheduler initialized.")

# ======== FORECAST WRAPPER =========
def run_forecast_task():
    try:
        print("📈 [SCHEDULER] Running weather forecast script...")
        logging.info("📈 Forecast run started.")
        run_forecast()
        logging.info("✅ Forecast completed successfully.")
    except Exception as e:
        print("❌ [SCHEDULER ERROR] Forecast failed:", str(e))
        logging.error(f"❌ Forecast error: {e}")
