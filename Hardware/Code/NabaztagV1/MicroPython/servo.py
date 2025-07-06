from machine import Pin, PWM

class SERVO:
    def __init__(self, pin, freq=50, min_us=500, max_us=2500, max_angle=180):
        self.pwm = PWM(Pin(pin))
        self.pwm.freq(freq)
        self.freq = freq
        self.min_us = min_us
        self.max_us = max_us
        self.max_angle = max_angle  # 180° typique pour SG90

    def angle_to_duty_u16(self, angle):
        # Clamp à la plage valide
        angle = max(0, min(angle, self.max_angle))
        us = self.min_us + (angle / self.max_angle) * (self.max_us - self.min_us)
        period_us = 1000000 // self.freq
        duty_ratio = us / period_us  # rapport cyclique
        duty_u16 = int(duty_ratio * 65535)
        return duty_u16

    def set_angle(self, angle):
        """Déplace le servo à un angle entre 0 et 180°"""
        if angle > self.max_angle:
            print(f"[!] Angle {angle}° limité à {self.max_angle}°")
        angle = max(0, min(angle, self.max_angle))
        duty = self.angle_to_duty_u16(angle)
        self.pwm.duty_u16(duty)

    def set_angle_360(self, angle):
        """Permet un mouvement cyclique sur la plage 0–180°"""
        mapped_angle = angle % 180
        self.set_angle(mapped_angle)

    def deinit(self):
        self.pwm.deinit()
