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
wf = wifi.WIFI("bobox", "mon joli mot de passe")

wf.connect()

while not wf.isconnected():
    if (wf.status() == 0):
        scr.log("wifi not enabled")
    elif (wf.status() == 1):
        scr.log("currently scanning")
    elif (wf.status() == 2):
        scr.log("connecting to a network")
    if (wf.status() == 3):
        scr.log("connected to a network")
    elif (wf.status() == 4):
        scr.log("connection failed")
    time.sleep(1)

np.setColor(0, 0, lightPower, 0)
np.setColor(1, 0, lightPower, 0)
np.setColor(2, 0, lightPower, 0)

meteo = weather.WEATHER(latitude=45.7334, longitude=4.2275)

earLeft = servo.SERVO(pin=18)
earRight = servo.SERVO(pin=22)

while True:
    earLeft.forward(0.5)
    earRight.forward(0.5)
    time.sleep_ms(500)
    earLeft.stop()
    earLeft.backward(0.5)
    earRight.backward(0.5)
    time.sleep_ms(500)
    earLeft.stop()
    earRight.stop()

    meteo_data = meteo.getWeatherData()
    np.setWeather(meteo.getWeatherTypeFromCode(meteo_data["next"]["weather_code"]))
    scr.cls()
    scr.text(f"Temp: {meteo_data["current"]["temperature_2m"]}C", 0, 0)
    scr.text(f"Type: {meteo.getWeatherTypeFromCode(meteo_data["current"]["weather_code"])}", 0, 20)
    scr.disp()
    time.sleep(300)
    print("coucou")