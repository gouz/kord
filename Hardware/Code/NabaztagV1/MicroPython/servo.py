from machine import Pin, PWM
from time import sleep_ms

class SERVO:
    def __init__(self, pin:int):
        self.pwm = PWM(Pin(pin, mode=Pin.OUT))
        self.pwm.freq(50)
        self.pwm.duty_u16(0)
        self.current_position = 0

    def rp_cy(self, angle):
        temps_haut = (2000/180) * angle + 500
        rp_cyclique = (temps_haut / 20000) * 100
        return int((rp_cyclique / 100) * 65535)

    def move_to_position(self, angle:int, speed_ms: int):
        delta = angle - self.current_position
        nb_iterations = int(speed_ms / 10)
        for i in range(nb_iterations):
            self.current_position = self.current_position + (delta / nb_iterations)
            self.pwm.duty_u16(self.rp_cy(self.current_position))
            sleep_ms(10)