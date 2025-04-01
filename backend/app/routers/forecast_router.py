from fastapi import APIRouter, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.responses import JSONResponse
from app.services.weather_api import get_weather
import csv
import os
import httpx
import asyncio
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

router = APIRouter()

WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


@router.get("/forecast")
async def get_7_day_forecast():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.abspath(os.path.join(base_dir, "../ml/weather_ml/forecast/weather_forecast_results.csv"))

    if not os.path.exists(csv_path):
        return JSONResponse(status_code=404, content={"message": "Forecast result not found"})

    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]

    # Sort by date and limit to the first 7 entries
    forecast_data = sorted(data, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d'))[:7]

    return {"forecast": forecast_data}


@router.get("/weather")
async def get_weather():
   # Use lat/lon of Parang, Calapan City, Oriental Mindoro
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
            response = await client.get(WEATHER_API_URL, params=params)
            response.raise_for_status()
    except httpx.HTTPError as e:
        print("[ERROR] Weather API request failed:", e)
        raise HTTPException(status_code=500, detail="Weather API unavailable")

    data = response.json()
    current = data["current"]
    location = data["location"]

    weather_info = {
        "location": location["name"],
        "region": location["region"],
        "country": location["country"],
        "temperature_c": current["temp_c"],
        "temperature_f": current["temp_f"],
        "humidity": current["humidity"],
        "wind_speed_kph": current["wind_kph"],
        "wind_speed_ms": round(current["wind_kph"] / 3.6, 2),
        "pressure_hpa": current["pressure_mb"],
        "cloud_cover_percent": current["cloud"],
        "weather_condition": current["condition"]["text"],
        "rain_mm": current.get("precip_mm", 0),
        "uv": current.get("uv", 0),
        "last_updated": current.get("last_updated")
    }

    print("[DEBUG] Current weather:", weather_info)
    return weather_info 

clients = []

@router.websocket("/ws/weather")
async def websocket_weather(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            await asyncio.sleep(300)
            try:
                weather_info = await get_weather()
                print("[DEBUG] Sending weather update to client")

                disconnected_clients = []
                for client in clients:
                    try:
                        await client.send_json(weather_info)
                    except Exception as e:
                        print("[ERROR] Skipping disconnected client:", e)
                        disconnected_clients.append(client)

                for dead_client in disconnected_clients:
                    clients.remove(dead_client)

            except Exception as e:
                print("[ERROR] Weather update failed:", e)
    except WebSocketDisconnect:
        print("[INFO] WebSocket disconnect caught")
        if websocket in clients:
            clients.remove(websocket)
