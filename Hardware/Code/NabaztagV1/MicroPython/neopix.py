from machine import Pin
import neopixel
import random
import time
import _thread


class NEOPIX:
    def __init__(self, lightPower):
        self.animation = False
        self.lightPower = lightPower
        self.nbPixels = 3
        self.np = neopixel.NeoPixel(Pin(20), self.nbPixels)
        for i in range(self.nbPixels):
            self.np[i] = (0, 0, 0)
        self.np.write()

    def setColor(self, num, r, g, b):
        self.np[num] = (r, g, b)
        self.np.write()

    def stopAnimation(self):
        self.animation = False
        time.sleep(1.1)

    def setWeather(self, weather_type):
        self.stopAnimation()
        time.sleep(1)
        if (weather_type == "clear"):
            # 3 yellow
            self.setColor(0, self.lightPower, self.lightPower, 0)
            self.setColor(1, self.lightPower, self.lightPower, 0)
            self.setColor(2, self.lightPower, self.lightPower, 0)
        elif (weather_type == "cloudy"):
            # Blue Yellow Blue
            self.setColor(0, 0, 0, self.lightPower)
            self.setColor(1, self.lightPower, self.lightPower, 0)
            self.setColor(2, 0, 0, self.lightPower)
        elif (weather_type == "rain"):
            # Blue blink random
            def rainBlink():
                while self.animation:
                    for i in range(3):
                        self.setColor(i, 0, 0, 0)
                    self.setColor(random.randint(0, 2), 0, 0, self.lightPower)
                    time.sleep(1)
            self.animation = True
            _thread.start_new_thread(rainBlink, ())
        elif (weather_type == "fog"):
            # Blue blink
            def fogBlink():
                while self.animation:
                    for i in range(3):
                        self.setColor(i, 0, 0, 0)
                    time.sleep(1)
                    for i in range(3):
                        self.setColor(i, 0, 0, self.lightPower)
                    time.sleep(1)
            self.animation = True
            _thread.start_new_thread(fogBlink, ())
        elif (weather_type == "thunderstorm"):
            # Blue yellow random
            def thunderBlink():
                while self.animation:
                    for i in range(3):
                        self.setColor(i, 0, 0, self.lightPower)
                    self.setColor(random.randint(0, 2), self.lightPower, self.lightPower, 0)
                    time.sleep(1)
            self.animation = True
            _thread.start_new_thread(thunderBlink, ())
        elif (weather_type == "snow"):
            # blue middle
            def snowBlink():
                while self.animation:
                    self.setColor(0, 0, 0, 0)
                    self.setColor(2, 0, 0, 0)
                    self.setColor(1, 0, 0, self.lightPower)
                    time.sleep(1)
                    self.setColor(1, 0, 0, 0)
                    time.sleep(1)
            self.animation = True
            _thread.start_new_thread(snowBlink, ())