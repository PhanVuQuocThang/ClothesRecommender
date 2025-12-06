import requests

# --- WEATHER CODE MAP ---
WEATHER_CODE_MAP = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Light freezing drizzle",
    57: "Dense freezing drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
    77: "Snow grains",
    80: "Rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    85: "Snow showers",
    86: "Heavy snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm with hail",
    99: "Severe thunderstorm with hail"
}

# --- FETCH WEATHER DATA ---
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 21.028,
    "longitude": 105.834,
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,weathercode",
    "forecast_days": 14,
    "timezone": "Asia/Singapore"
}

response = requests.get(url, params=params)
data = response.json()
daily = data["daily"]

# --- FORMAT & PRINT ---
print("\n===== 14-Day Weather Forecast =====\n")

for i in range(len(daily["time"])):
    date = daily["time"][i]
    tmax = daily["temperature_2m_max"][i]
    tmin = daily["temperature_2m_min"][i]
    rain = daily["precipitation_sum"][i]
    code = daily["weathercode"][i]
    label = WEATHER_CODE_MAP.get(code, "Unknown")

    print(f"{date}")
    print(f"  · Weather: {label} (code {code})")
    print(f"  · Max Temp: {tmax}°C")
    print(f"  · Min Temp: {tmin}°C")
    print(f"  · Rain: {rain} mm")
    print()
