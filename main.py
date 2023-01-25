import requests
import json


class OpenWeatherMapApi:
    def __init__(self):
        self.api_key = "45c7cef18d074acb6f50f563fd6a6f9f"
        self.lat = 48.208176
        self.lon = 16.373

    def get_weather(self):
        response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params={"lat": self.lat, "lon": self.lon, "appid": self.api_key })
        json_weather = response.json()
        return json_weather



