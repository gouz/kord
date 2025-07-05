from machine import Pin, I2C #, PWM
import neopixel
import network
import urequests as requests
import ssd1306

nbPixels = 5
latitude = 45.7334
longitude = 4.2275
urlWeather = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,weather_code"

lightPower = 32

np = neopixel.NeoPixel(Pin(4), nbPixels)

# motor1 = PWM(Pin(10, mode=Pin.OUT))
# motor1.freq(50)
# motor2 = PWM(Pin(12, mode=Pin.OUT))
# motor2.freq(50)

for i in range(nbPixels):
    np[i] = (0, 0, 0)
np.write()

np[4] = (127, 0, 0)
np.write()

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('bobox', 'mon joli mot de passe')
while not wlan.isconnected():
    pass
print("Connected to Wi-Fi")
np[4] = (0, lightPower, 0)
np.write()

i2c = I2C(0, sda=Pin(16), scl=Pin(17)) 


oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('Hello, World 1!', 0, 0)
oled.text('Hello, World 2!', 0, 10)
oled.text('Hello, World 3!', 0, 20)

oled.show()

weather = requests.get(urlWeather)
print(f"Réponse du serveur : {weather.json()}")

# if (weather == 800):
#     np[0] = (lightPower, lightPower, 0)
#     np[1] = (lightPower, lightPower, 0)
#     np[2] = (lightPower, lightPower, 0)
# elif (weather > 800):
#     np[0] = (0, 0, lightPower)
#     np[1] = (lightPower, lightPower, 0)
#     np[2] = (0, 0, lightPower)

# np.write()

# while True:
#     motor1.duty_u16(1638)
#     motor2.duty_u16(7864)
#     sleep(1)
#     motor1.duty_u16(7864)
#     motor2.duty_u16(1638)
#     sleep(1)