from machine import Pin, I2C
import ssd1306

class SCREEN:
    def __init__(self):
        i2c = I2C(0, sda=Pin(16), scl=Pin(17)) 
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