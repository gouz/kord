import wifi
import neopix
import weather
import time
import servo
import screen
import taichi
import button
import icons

ics = icons.ICONS()

earLeft = servo.SERVO(pin=18)
earRight = servo.SERVO(pin=22)

scr = screen.SCREEN(sda=16, scl=17)

myButton = button.BUTTON(pin=14)

lightPower = 16
np = neopix.NEOPIX(pin=20, lightPower=lightPower)
np.setColor(0, lightPower, 0, 0)
np.setColor(1, lightPower, 0, 0)
np.setColor(2, lightPower, 0, 0)

tai = taichi.TAICHI(np, earLeft, earRight, lightPower)

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

scr.log("connected")

np.setColor(0, 0, lightPower, 0)
np.setColor(1, 0, lightPower, 0)
np.setColor(2, 0, lightPower, 0)

meteo = weather.WEATHER(latitude=45.7334, longitude=4.2275)

mode = "weather"

cptRefresh = 0

while True:
    if myButton.isPressed():
        if mode == "weather": 
            mode = "taichi"
            scr.cls()
            scr.log(mode)
        else: mode = "weather"
    
    if mode == "weather":
        tai.stop()
        if cptRefresh == 300 or cptRefresh == 0:
            cptRefresh = 0
            scr.cls()
            scr.log("get weather")
            meteo_data = meteo.getWeatherData()
            np.setWeather(meteo.getWeatherTypeFromCode(meteo_data["next"]["weather_code"]))
            scr.cls()
            scr.img(ics.img(meteo.getWeatherTypeFromCode(meteo_data["current"]["weather_code"])), 0, 0)
            scr.text(f"{meteo_data["current"]["temperature_2m"]}C", 70, 28)
            scr.disp()
        cptRefresh = cptRefresh + 1
    elif mode == "taichi":
        cptRefresh = 0
        tai.go()
    time.sleep(1)
