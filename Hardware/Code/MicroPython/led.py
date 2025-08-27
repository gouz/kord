import neopixel
from time import sleep_ms

class Led:
    def __init__(self, pin, num_leds):
        self.num_leds = num_leds
        self.np = neopixel.NeoPixel(pin, num_leds)
    
    def set_color_all(self, color):
        for i in range(self.num_leds):
            self.np[i] = color # type: ignore
        self.np.write()
    
    def set_color(self, led_index, color):
        if led_index < 0 or led_index >= self.num_leds:
            raise ValueError("LED index out of range")
        self.np[led_index] = color # type: ignore
        self.np.write()

    def waveColor(self, led_index, delay=100):
        while True:
            for i in range(256):
                self.set_color(led_index, (i, 0, 0))
                sleep_ms(delay)
            for i in range(255, -1, -1):
                self.set_color(led_index, (i, 0, 0))
                sleep_ms(delay)