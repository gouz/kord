import wifi
import screen
import microsd
# import neopix

# lightPower = 32
# np = neopix.NEOPIX()
# np.setColor(4, lightPower, 0, 0)

scr = screen.SCREEN()

scr.log("SD read")
sd = microsd.MICROSD()

config = sd.getConfig()

scr.log("WiFi connection")

wifi.WIFI(config["WIFI_SSID"], config["WIFI_PWD"])
scr.log("connected")

# np.setColor(4, 0, lightPower, 0)