from machine import Pin, I2C
import ssd1306
import framebuf

class SCREEN:
    def __init__(self, sda, scl):
        i2c = I2C(0, sda=Pin(sda), scl=Pin(scl)) 
        self.oled = ssd1306.SSD1306_I2C(128, 64, i2c)

    def text(self, str, x = 0, y = 0):
        self.oled.text(str, x, y)

    def disp(self):
        self.oled.show()
    
    def cls(self):
        self.oled.fill(0)
        self.disp()

    def log(self, str):
        self.cls()
        self.text(str, 0, 0)
        self.disp()

    def img(self, imagebuffer, left, top):
        fb = framebuf.FrameBuffer(bytearray(imagebuffer), 64, 64, framebuf.MONO_HLSB)
        for y in range(64):
            for x in range(64):
                pixel = fb.pixel(x, y)
                self.oled.pixel(left + x, top + y, pixel)
        self.oled.show()