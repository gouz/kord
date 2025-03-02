import neopixel
from machine import Pin
import time

pixels = neopixel.NeoPixel(Pin(4), 5)
led = 0
direction = 1
while True:
    pixels.fill((0, 0, 0))
    pixels[led%5]=(0, 0, 255)
    pixels.write()
    if (led == 4):
        direction = -1
    elif (led == 0):
        direction = 1
    led = led + 1 * direction
    time.sleep_ms(100)
    