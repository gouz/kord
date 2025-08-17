import wifi
import neopix
import weather
import time
import servo
import screen
import taichi
import button
import icons
import microsd
import sys

scr = screen.SCREEN(sda=16, scl=17)
scr.log("init")

sd = None
try:
    sd = microsd.MICROSD()
except Exception as e:
    scr.log(f'err: {e}')
    print(e)
    sys.exit(1)

config = {}
if sd != None:
    config = sd.getConfig()
if config == {}:
    scr.log("error read sd")
else:
    ics = icons.ICONS()
    earLeft = servo.SERVO(pin=18)
    earRight = servo.SERVO(pin=22)
    myButton = button.BUTTON(pin=14)
    lightPower = 64
    np = neopix.NEOPIX(pin=20, lightPower=lightPower)
    np.setColor(0, lightPower, 0, 0)
    np.setColor(1, lightPower, 0, 0)
    np.setColor(2, lightPower, 0, 0)
    earLeft.forward(0.1)
    earRight.backward(0.1)
    tai = taichi.TAICHI(np, earLeft, earRight, lightPower)
    scr.log("WiFi connection")
    wf = wifi.WIFI(config["WIFI_SSID"], config["WIFI_PWD"])
    wf.connect()
    while not wf.isconnected():
        if (wf.status() == 0):
            scr.log("wifi not enabled")
        elif (wf.status() == 1):
            scr.log("scanning")
        elif (wf.status() == 2):
            scr.log("connecting")
        if (wf.status() == 3):
            scr.log("connected")
        elif (wf.status() == 4):
            scr.log("failed")
        time.sleep(1)
    scr.log("connected")
    earLeft.stop()
    earRight.stop()
    np.setColor(0, 0, lightPower, 0)
    np.setColor(1, 0, lightPower, 0)
    np.setColor(2, 0, lightPower, 0)
    meteo = weather.WEATHER(latitude=float(config["GPS_LATITUDE"]), longitude=float(config["GPS_LONGITUDE"]))
    mode = "weather"
    cptRefresh = 0
    while True:
        if myButton.isPressed():
            if mode == "weather": 
                mode = "taichi"
                scr.cls()
                scr.log(mode)
                np.stopAnimation()
            else: mode = "weather"
        if mode == "weather":
            tai.stop()
            if cptRefresh >= 900 or cptRefresh == 0: # open-meteo 15 min refresh
                cptRefresh = 0
                scr.cls()
                scr.log("get weather")
                np.stopAnimation()
                meteo_data = meteo.getWeatherData()
                np.setWeather(meteo.getWeatherTypeFromCode(meteo_data["next"]["weather_code"]))
                scr.cls()
                scr.img(ics.img(meteo.getWeatherTypeFromCode(meteo_data["current"]["weather_code"])), 0, 0)
                scr.text(f"{meteo_data["current"]["temperature_2m"]}C", 70, 28)
                scr.text(f"{meteo_data["current"]["time"].strip()[11:16]}", 84, 45)
                scr.disp()
            cptRefresh = cptRefresh + 1
        elif mode == "taichi":
            cptRefresh = 0
            tai.go()
        time.sleep(1)
