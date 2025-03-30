
import requests
import pandas as pd
from datetime import datetime

# Coordinates for Parang, Calapan City, Oriental Mindoro
LATITUDE = 13.3945574
LONGITUDE = 121.1870931


# Date range from 2015 to current date
start_date = "2015-01-01"
end_date = datetime.now().strftime("%Y-%m-%d")

# Updated API request with additional precipitation parameters
url = f"https://archive-api.open-meteo.com/v1/archive?latitude={LATITUDE}&longitude={LONGITUDE}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,precipitation_hours,snowfall_sum,wind_speed_10m_max,cloud_cover_mean,relative_humidity_2m_mean,surface_pressure_mean&timezone=Asia/Manila"

response = requests.get(url)
data = response.json()

if "daily" in data:
    df = pd.DataFrame({
        "date": data["daily"]["time"],
        "temperature_max": data["daily"]["temperature_2m_max"],
        "temperature_min": data["daily"]["temperature_2m_min"],
        "rainfall": data["daily"]["precipitation_sum"],
        "precipitation_hours": data["daily"]["precipitation_hours"],  # New
        "snowfall": data["daily"]["snowfall_sum"],  # New (likely 0s in PH)
        "wind_speed": data["daily"]["wind_speed_10m_max"],
        "cloud_cover": data["daily"]["cloud_cover_mean"],
        "humidity": data["daily"]["relative_humidity_2m_mean"],
        "pressure": data["daily"]["surface_pressure_mean"]
    })
    
    df.to_csv("dataset.csv", index=False)
    print(f"✅ Historical data ({start_date} to {end_date}) saved successfully!")
else:
    print("❌ Error:", data.get("reason", "Unknown API error"))

