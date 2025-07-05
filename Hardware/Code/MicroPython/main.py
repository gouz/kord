import wifi
import screen
import microsd

scr = screen.SCREEN()

scr.log("SD read")
sd = microsd.MICROSD()

config = sd.getConfig()

scr.log("WiFi connection")

ip = wifi.WIFI(config["WIFI_SSID"], config["WIFI_PWD"])
scr.log("connected")
