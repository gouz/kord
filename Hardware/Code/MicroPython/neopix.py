from machine import Pin
import neopixel
import random
import time
import _thread

class NEOPIX:
    def __init__(self, pin, lightPower):
        self.animation = False
        self.lightPower = lightPower
        self.nbPixels = 3
        self.np = neopixel.NeoPixel(pin= Pin(pin, mode=Pin.OUT), n=self.nbPixels, bpp= 3, timing=1)
        for i in range(self.nbPixels):
            self.np[i] = (0, 0, 0)
        self.np.write()

    def setColor(self, num, r, g, b, disp = True):
        self.np[num] = (r, g, b)
        if (disp):
            self.np.write()

    def write(self):
        self.np.write()

    def stopAnimation(self):
        self.animation = False
        time.sleep(2.1)

    def setWeather(self, weather_type):
        self.stopAnimation()
        time.sleep(2)
        if (weather_type == "clear"):
            # 3 yellow
            self.setColor(0, self.lightPower, self.lightPower, 0, False)
            self.setColor(1, self.lightPower, self.lightPower, 0, False)
            self.setColor(2, self.lightPower, self.lightPower, 0, False)
            self.write()
        elif (weather_type == "cloudy"):
            # Blue Yellow Blue
            self.setColor(0, 0, 0, self.lightPower, False)
            self.setColor(1, self.lightPower, self.lightPower, 0, False)
            self.setColor(2, 0, 0, self.lightPower, False)
            self.write()
        elif (weather_type == "rain"):
            # Blue blink random
            def rainBlink():
                while self.animation:
                    for i in range(3):
                        self.setColor(i, 0, 0, 0, False)
                    self.setColor(random.randint(0, 2), 0, 0, self.lightPower, False)
                    self.write()
                    time.sleep(2)
            self.animation = True
            _thread.start_new_thread(rainBlink, ())
        elif (weather_type == "fog"):
            # Blue blink
            def fogBlink():
                while self.animation:
                    for i in range(3):
                        self.setColor(i, 0, 0, 0, False)
                    self.write()
                    time.sleep(2)
                    for i in range(3):
                        self.setColor(i, 0, 0, self.lightPower, False)
                    self.write()
                    time.sleep(2)
            self.animation = True
            _thread.start_new_thread(fogBlink, ())
        elif (weather_type == "thunderstorm"):
            # Blue yellow random
            def thunderBlink():
                while self.animation:
                    for i in range(3):
                        self.setColor(i, 0, 0, self.lightPower, False)
                    self.setColor(random.randint(0, 2), self.lightPower, self.lightPower, 0, False)
                    self.write()
                    time.sleep(2)
            self.animation = True
            _thread.start_new_thread(thunderBlink, ())
        elif (weather_type == "snow"):
            # blue middle
            def snowBlink():
                while self.animation:
                    self.setColor(0, 0, 0, 0, False)
                    self.setColor(2, 0, 0, 0, False)
                    self.setColor(1, 0, 0, self.lightPower, False)
                    self.write()
                    time.sleep(2)
                    self.setColor(1, 0, 0, 0, False)
                    self.write()
                    time.sleep(2)
            self.animation = True
            _thread.start_new_thread(snowBlink, ())