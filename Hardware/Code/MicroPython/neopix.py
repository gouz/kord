from machine import Pin
import neopixel
import random

class NEOPIX:
    def __init__(self, pin, lightPower):
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

    def setWeather(self, weather_type):
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
            for i in range(3):
                self.setColor(i, 0, 0, 0, False)
            self.setColor(random.randint(0, 2), 0, 0, self.lightPower, False)
            self.write()
        elif (weather_type == "fog"):
            # Blue blink
            for i in range(3):
                self.setColor(i, 0, 0, 0, False)
            self.write()
            time.sleep(1)
            for i in range(3):
                self.setColor(i, 0, 0, self.lightPower, False)
            self.write()
            time.sleep(1)
        elif (weather_type == "thunderstorm"):
            # Blue yellow random
            for i in range(3):
                self.setColor(i, 0, 0, self.lightPower, False)
            self.setColor(random.randint(0, 2), self.lightPower, self.lightPower, 0, False)
            self.write()
        elif (weather_type == "snow"):
            # blue middle
            self.setColor(0, 0, 0, 0, False)
            self.setColor(2, 0, 0, 0, False)
            self.setColor(1, 0, 0, self.lightPower, False)
            self.write()
            time.sleep(1)
            self.setColor(1, 0, 0, 0, False)
            self.write()
            time.sleep(1)