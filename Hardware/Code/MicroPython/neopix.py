from machine import Pin
import neopixel

class NEOPIX:
    def __init__(self):
        self.nbPixels = 5
        self.np = neopixel.NeoPixel(Pin(20), 5)
        for i in range(self.nbPixels):
            self.np[i] = (0, 0, 0)
        self.np.write()

    def setColor(self, num, r, g, b):
        self.np[num] = (r, g, b)
        self.np.write()