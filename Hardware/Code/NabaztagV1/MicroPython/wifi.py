from network import WLAN, STA_IF
from time import sleep

class WIFI:
    def __init__(self, login, password):
        wlan = WLAN(STA_IF)
        wlan.active(True)
        wlan.connect(login, password)
        while not wlan.isconnected():
            sleep(1)