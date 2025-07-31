from machine import Pin


class BUTTON:
    def __init__(self, pin):
        self.pin = Pin(pin, Pin.IN, Pin.PULL_UP)

    def isPressed(self):
        return not self.pin.value()