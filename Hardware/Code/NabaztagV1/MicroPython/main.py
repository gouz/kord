import wifi
import neopix
import weather
import time
import servo

lightPower = 64
np = neopix.NEOPIX(pin=20, lightPower=lightPower)
np.setColor(0, lightPower, 0, 0)
np.setColor(1, lightPower, 0, 0)
np.setColor(2, lightPower, 0, 0)

wifi.WIFI("bobox", "mon joli mot de passe")

np.setColor(0, 0, lightPower, 0)
np.setColor(1, 0, lightPower, 0)
np.setColor(2, 0, lightPower, 0)

meteo = weather.WEATHER(latitude=45.7334, longitude=4.2275)
weather_type = meteo.getWeatherTypeFromCode(meteo.getWeatherData()["weather_code"])

np.setWeather(weather_type)

earLeft = servo.SERVO(pin=18)
earRight = servo.SERVO(pin=22)

while True:
    earLeft.forward(0.5)
    earRight.forward(0.5)
    time.sleep_ms(500)
    earLeft.backward(1.0)
    earRight.backward(1.0)
    time.sleep_ms(1000)
