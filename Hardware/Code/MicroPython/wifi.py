import network

class WIFI:
    def __init__(self, login, password):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(login, password)
        while not wlan.isconnected():
            pass
        print("connected")