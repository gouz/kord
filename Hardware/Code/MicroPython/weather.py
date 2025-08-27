import urequests as requests

class WEATHER:
    def __init__(self, latitude, longitude):
        self.urlWeather = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,weather_code&hourly=temperature_2m,weather_code&timezone=auto&forecast_days=2"

    def getWeatherData(self) -> dict:
        weather = requests.get(self.urlWeather)
        data = weather.json()
        times = data["hourly"]["time"]
        temperatures = data["hourly"]["temperature_2m"]
        weather_codes = data["hourly"]["weather_code"]
        weather_data = [
            {
                "time": time.strip()[0:13],
                "temperature_2m": temp,
                "weather_code": code
            }
            for time, temp, code in zip(times, temperatures, weather_codes)
        ]
        current = weather.json()["current"]["time"].strip()[0:13]
        i = 0
        while (weather_data[i]["time"] != current):
           i += 1
        return {
            "next": weather_data[i + 1],
            "current": weather.json()["current"]
        }
    
    def getWeatherTypeFromCode(self, code):
        if (code >= 90):
            return "thunderstorm"
        if (code >= 85):
            return "snow"
        if (code >= 80):
            return "rain"
        if (code >= 70):
            return "snow"
        if (code >= 60):
            return "rain"
        if (code >= 50):
            return "drizzle"
        if (code >= 40):
            return "fog"
        if (code >= 1):
            return "cloudy"
        return "clear"
