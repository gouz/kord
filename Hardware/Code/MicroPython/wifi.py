from network import WLAN, STA_IF
from time import sleep

class WIFI:
    def __init__(self, login, password):
        self.wlan = WLAN(STA_IF)
        self.wlan.config(pm = 0xa11140)
        self.wlan.active(True)
        self.login = login
        self.password = password
    
    def connect(self):
        self.wlan.connect(self.login, self.password)
        
    def isconnected(self):
        return self.wlan.isconnected()
    
    def status(self):
        return self.wlan.status()
