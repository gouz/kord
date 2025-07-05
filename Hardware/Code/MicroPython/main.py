import neopix
import wifi
import screen
import microsd

lightPower = 32

scr = screen.SCREEN()

scr.log("SD read")
microsd.MICROSD()

np = neopix.NEOPIX()
np.setColor(4, lightPower, 0, 0)

scr.log("WiFi connection")

wifi.WIFI('bobox', 'mon joli mot de passe')
np.setColor(4, 0, lightPower, 0)

scr.log("connected")
