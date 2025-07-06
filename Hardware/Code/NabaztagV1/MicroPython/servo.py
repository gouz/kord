from machine import Pin, PWM

class SERVO:
    def __init__(self, pin, freq=50, stop_us=1500, min_us=1000, max_us=2000):
        self.pwm = PWM(Pin(pin))
        self.pwm.freq(freq)
        self.freq = freq
        self.min_us = min_us
        self.max_us = max_us
        self.stop_us = stop_us

    def send_us(self, us):
        # Convertit le temps d’impulsion en duty_u16
        period_us = 1000000 // self.freq
        duty = int((us / period_us) * 65535)
        self.pwm.duty_u16(duty)

    def stop(self):
        self.send_us(self.stop_us)

    def forward(self, speed=1.0):
        """Tourne en avant — speed entre 0.0 (stop) et 1.0 (max)"""
        us = self.stop_us + speed * (self.max_us - self.stop_us)
        self.send_us(us)

    def backward(self, speed=1.0):
        """Tourne en arrière — speed entre 0.0 (stop) et 1.0 (max)"""
        us = self.stop_us - speed * (self.stop_us - self.min_us)
        self.send_us(us)

    def deinit(self):
        self.pwm.deinit()