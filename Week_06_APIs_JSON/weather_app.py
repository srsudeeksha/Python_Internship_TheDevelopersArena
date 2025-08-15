# weather_app.py
# Week 6 Task – Weather App using API and JSON

import requests

def get_weather(city, api_key):
    """
    Fetch weather data for a given city using OpenWeatherMap API.
    
    Args:
        city (str): City name
        api_key (str): Your OpenWeatherMap API key
    
    Returns:
        dict: Weather details if found, else None
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Temperature in Celsius
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"⚠️ HTTP error: {err}")
    except requests.exceptions.RequestException as err:
        print(f"⚠️ Request error: {err}")
    return None


def display_weather(data):
    """
    Display weather details in a user-friendly format.
    
    Args:
        data (dict): JSON weather data
    """
    city = data["name"]
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    weather = data["weather"][0]["description"].title()

    print(f"\n📍 Weather in {city}, {country}")
    print(f"🌡️ Temperature: {temp}°C (Feels like {feels_like}°C)")
    print(f"⛅ Condition: {weather}")


def main():
    print("🌦️ Weather App (Week 6 Project)")
    api_key = input("Enter your OpenWeatherMap API Key: ").strip()
    city = input("Enter city name: ").strip()

    weather_data = get_weather(city, api_key)

    if weather_data and weather_data.get("cod") == 200:
        display_weather(weather_data)
    else:
        print("❌ Could not fetch weather data. Please check the city name or API key.")


if __name__ == "__main__":
    main()
