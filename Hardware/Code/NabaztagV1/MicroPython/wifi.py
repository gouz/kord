from network import WLAN, STA_IF
from time import sleep

class WIFI:
    def __init__(self, login, password):
        wlan = WLAN(STA_IF)
        wlan.config(pm = 0xa11140)
        wlan.active(True)
        wlan.connect(login, password)
        while not wlan.isconnected():
            sleep(1)