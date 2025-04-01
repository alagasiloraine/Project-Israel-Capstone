# from fastapi import FastAPI, HTTPException, WebSocket
# from fastapi.middleware.cors import CORSMiddleware
# import os
# import httpx
# import asyncio
# import serial
# import json
# import logging

# from dotenv import load_dotenv
# from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.triggers.cron import CronTrigger
# import subprocess

# from app.services.firebase_service import firebase_admin
# from app.routers import crop_router, auth_router, forecast_router, sensor_data, npk_router
# from app.ml.weather_ml.forecast.forecast import main as run_forecast

# # ======== ENV & LOG SETUP ===========
# load_dotenv()
# WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
# if not WEATHER_API_KEY:
#     raise ValueError("WEATHER_API_KEY is not set. Please check your .env file.")

# logging.basicConfig(
#     filename="forecast_log.txt",
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )

# logger = logging.getLogger(__name__)

# # ======== FASTAPI APP SETUP =========
# app = FastAPI(title="Crop Recommendation API")

# # ======== CORS CONFIG =========
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # ======== ROUTERS =========
# app.include_router(crop_router.router, prefix="/api/crop", tags=["crop"])
# app.include_router(auth_router.router, prefix="/api/auth", tags=["auth"])
# app.include_router(forecast_router.router, prefix="/api/weather", tags=["weather"])
# # app.include_router(npk_router.router, prefix="/api/npk", tags=["npk"])
# app.include_router(sensor_data.router)

# # ======== MIDDLEWARE FOR WS =========
# @app.middleware("http")
# async def allow_websocket_cors(request, call_next):
#     if request.scope["type"] == "websocket":
#         return await npk_router.websocket_endpoint(request)
#     return await call_next(request)

# # ======== SCHEDULER JOB =========
# def schedule_forecast_script():
#     logger.info("⏳ Running scheduled weather forecasting...")
#     try:
#         run_forecast()
#         logger.info("✅ Forecasting completed successfully.")
#     except Exception as e:
#         logger.error(f"❌ Forecasting failed: {e}")

# scheduler = BackgroundScheduler()
# scheduler.add_job(schedule_forecast_script, CronTrigger(day_of_week='sun', hour=0, minute=0))  # Every Sunday at 00:00
# scheduler.start()

# # ======== ROUTES =========
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
#     latitude = 13.3945574
#     longitude = 121.1870931
#     coordinates = f"{latitude},{longitude}"
#     # location = "Parang, Calapan City, Oriental Mindoro"

#     params = {
#         "key": WEATHER_API_KEY,
#         "q": coordinates,
#         "aqi": "no"
#     }

#     try:
#         async with httpx.AsyncClient(timeout=10.0) as client:
#             response = await client.get("http://api.weatherapi.com/v1/current.json", params=params)
#             response.raise_for_status()
#     except httpx.RequestError as e:
#         raise HTTPException(status_code=500, detail=f"Weather API error: {e}")

#     weather_data = response.json()
#     wind_speed_kph = weather_data["current"]["wind_kph"]
#     wind_speed_ms = round(wind_speed_kph / 3.6, 2)

#     return {
#         "location": weather_data["location"]["name"],
#         "region": weather_data["location"]["region"],
#         "country": weather_data["location"]["country"],
#         "temperature_c": weather_data["current"]["temp_c"],
#         "temperature_f": weather_data["current"]["temp_f"],
#         "humidity": weather_data["current"]["humidity"],
#         "wind_speed_kph": wind_speed_kph,
#         "wind_speed_ms": wind_speed_ms,
#         "pressure_hpa": weather_data["current"]["pressure_mb"],
#         "cloud_cover_percent": weather_data["current"]["cloud"],
#         "weather_condition": weather_data["current"]["condition"]["text"],
#         "rain_mm": weather_data["current"].get("precip_mm", 0),
#         "uv": weather_data["current"].get("uv", 0),
#         "last_updated": weather_data["current"].get("last_updated")
#     }


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
from apscheduler.triggers.cron import CronTrigger
import subprocess

from app.services.firebase_service import firebase_admin
from app.routers import crop_router, auth_router, forecast_router, sensor_data, npk_router
from app.ml.weather_ml.forecast.forecast import main as run_forecast
from app.ml.weather_ml.forecast.get_dataset import main as update_dataset

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

logger = logging.getLogger(__name__)

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

# ======== SCHEDULER JOB =========
def schedule_forecast_script():
    logger.info("\u23f3 Running scheduled weather forecasting...")
    try:
        run_forecast()
        logger.info("\u2705 Forecasting completed successfully.")
    except Exception as e:
        logger.error(f"\u274c Forecasting failed: {e}")

def schedule_dataset_update():
    logger.info("\u23f3 Running scheduled dataset update...")
    try:
        update_dataset()
        logger.info("\u2705 Dataset updated successfully.")
    except Exception as e:
        logger.error(f"\u274c Dataset update failed: {e}")

scheduler = BackgroundScheduler()
scheduler.add_job(schedule_forecast_script, CronTrigger(day_of_week='sun', hour=0, minute=0))  # Every Sunday at 00:00
scheduler.add_job(schedule_dataset_update, CronTrigger(hour=0, minute=0))  # Every day at 00:00
scheduler.start()

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
    # latitude = 13.392611362807832
    # longitude = 121.22978104985009
    latitude = 13.401977220608616
    longitude = 121.22464223345575
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


# @app.get("/weather/")
# async def get_weather():
#     latitude = 13.3945574
#     longitude = 121.1870931

#     url = (
#         f"https://api.open-meteo.com/v1/forecast"
#         f"?latitude={latitude}&longitude={longitude}"
#         f"&current_weather=true"
#     )

#     try:
#         async with httpx.AsyncClient(timeout=10.0) as client:
#             response = await client.get(url)
#             response.raise_for_status()
#     except httpx.RequestError as e:
#         raise HTTPException(status_code=500, detail=f"Weather API error: {e}")

#     data = response.json()
#     current = data.get("current_weather")

#     if not current:
#         raise HTTPException(status_code=404, detail="Current weather data not available")

#     # Mapping Open-Meteo's weather code to description (optional)
#     weather_code_map = {
#         0: "Clear sky",
#         1: "Mainly clear",
#         2: "Partly cloudy",
#         3: "Overcast",
#         45: "Fog",
#         48: "Depositing rime fog",
#         51: "Light drizzle",
#         53: "Moderate drizzle",
#         55: "Dense drizzle",
#         61: "Slight rain",
#         63: "Moderate rain",
#         65: "Heavy rain",
#         71: "Slight snow fall",
#         73: "Moderate snow fall",
#         75: "Heavy snow fall",
#         80: "Slight rain showers",
#         81: "Moderate rain showers",
#         82: "Violent rain showers",
#         95: "Thunderstorm",
#         96: "Thunderstorm with slight hail",
#         99: "Thunderstorm with heavy hail",
#     }

#     weather_info = {
#         "location": "Parang, Calapan City",  # Hardcoded because Open-Meteo doesn't return location info
#         "region": "Oriental Mindoro",
#         "country": "Philippines",
#         "latitude": latitude,
#         "longitude": longitude,
#         "temperature_c": current["temperature"],
#         "temperature_f": round(current["temperature"] * 9/5 + 32, 1),
#         "humidity": current.get("humidity", 50.0),
#         "wind_speed_kph": round(current["windspeed"] * 3.6, 2),
#         "wind_speed_ms": current["windspeed"],
#         "pressure_hpa": current.get("pressure", 1013.0),
#         "cloud_cover_percent": current.get("cloud", 0.0),
#         "weather_condition": weather_code_map.get(current["weathercode"], "Unknown"),
#         "rain_mm": current.get("precip_mm", 0.0),
#         "uv": None,  # Open-Meteo doesn't provide UV index in the free tier
#         "last_updated": current["time"]
#     }


#     return weather_info



# ======== STARTUP HOOK =========
@app.on_event("startup")
async def on_startup():
    logger.info("🚀 FastAPI app started. Forecast scheduler is active.")


# ======== SERIAL READER =========
# SERIAL_PORT = 'COM3'
# BAUD_RATE = 4800

# async def read_serial_loop():
#     await asyncio.sleep(2)  # Allow FastAPI to fully start
#     try:
#         ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
#         print(f"✅ Connected to Arduino on {SERIAL_PORT}")
        
#         while True:
#             try:
#                 line = ser.readline().decode('utf-8').strip()
#                 if line:
#                     try:
#                         data = json.loads(line)
#                         await sensor_data.forward_sensor_data(data)
#                     except json.JSONDecodeError:
#                         print("⚠️ Invalid JSON:", line)
#             except Exception as e:
#                 print("❌ Error reading serial:", e)
#             await asyncio.sleep(0.1)

#     except Exception as e:
#         print("❌ Could not open serial port:", e)

# # ======== STARTUP EVENTS =========
# @app.on_event("startup")
# async def startup_event():
#     asyncio.create_task(read_serial_loop())

#     scheduler = BackgroundScheduler()
#     scheduler.add_job(run_forecast_task, 'interval', days=1)
#     scheduler.start()
#     print("📅 Forecast scheduler started (daily)")
#     logging.info("📅 Forecast scheduler initialized.")

# # ======== FORECAST WRAPPER =========
# def run_forecast_task():
#     try:
#         print("📈 [SCHEDULER] Running weather forecast script...")
#         logging.info("📈 Forecast run started.")
#         run_forecast()
#         logging.info("✅ Forecast completed successfully.")
#     except Exception as e:
#         print("❌ [SCHEDULER ERROR] Forecast failed:", str(e))
#         logging.error(f"❌ Forecast error: {e}")
