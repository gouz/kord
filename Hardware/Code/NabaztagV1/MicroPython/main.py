import wifi
import neopix
import weather
import time

lightPower = 64
np = neopix.NEOPIX(lightPower)
np.setColor(0, lightPower, 0, 0)
np.setColor(1, lightPower, 0, 0)
np.setColor(2, lightPower, 0, 0)

wifi.WIFI("bobox", "mon joli mot de passe")

np.setColor(0, 0, lightPower, 0)
np.setColor(1, 0, lightPower, 0)
np.setColor(2, 0, lightPower, 0)

latitude = 45.7334
longitude = 4.2275

meteo = weather.WEATHER(latitude, longitude)
weather_type = meteo.getWeatherTypeFromCode(meteo.getWeatherData()["weather_code"])

np.setWeather(weather_type)

time.sleep(5)
np.setWeather("clear")
time.sleep(5)
np.setWeather("cloudy")
time.sleep(5)
np.setWeather("rain")
time.sleep(5)
np.setWeather("fog")
time.sleep(5)
np.setWeather("thunderstorm")
time.sleep(5)
np.setWeather("snow")
time.sleep(5)
np.setWeather("clear")