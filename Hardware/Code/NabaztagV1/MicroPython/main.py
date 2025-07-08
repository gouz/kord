import wifi
import neopix
import weather
import time
import servo
import screen

scr = screen.SCREEN()

lightPower = 16
np = neopix.NEOPIX(pin=20, lightPower=lightPower)
np.setColor(0, lightPower, 0, 0)
np.setColor(1, lightPower, 0, 0)
np.setColor(2, lightPower, 0, 0)

scr.log("WiFi connection")
wifi.WIFI("bobox", "mon joli mot de passe")
scr.log("connected")

np.setColor(0, 0, lightPower, 0)
np.setColor(1, 0, lightPower, 0)
np.setColor(2, 0, lightPower, 0)

meteo = weather.WEATHER(latitude=45.7334, longitude=4.2275)

earLeft = servo.SERVO(pin=18)
earRight = servo.SERVO(pin=22)

while True:
    # earLeft.forward(0.5)
    # earRight.forward(0.5)
    # time.sleep_ms(500)
    # earLeft.backward(1.0)
    # earRight.backward(1.0)
    # time.sleep_ms(1000)

    meteo_data = meteo.getWeatherData()
    np.setWeather(meteo.getWeatherTypeFromCode(meteo_data["next"]["weather_code"]))
    scr.cls()
    scr.text(f"Temp: {meteo_data["current"]["temperature_2m"]}C", 0, 0)
    scr.text("Type: " + meteo.getWeatherTypeFromCode(meteo_data["current"]["weather_code"]), 0, 20)
    scr.disp()
    time.sleep(300)