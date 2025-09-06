from time import sleep
import random

class TAICHI:
    def __init__(self, np, earLeft, earRight, lightPower):
        self.np = np
        self.earLeft = earLeft
        self.earRight = earRight
        self.lightPower = lightPower
        random.seed()

    def go(self):
        self.np.setColor(0, random.randint(0, self.lightPower), random.randint(0, self.lightPower), random.randint(0, self.lightPower))
        self.np.setColor(1, random.randint(0, self.lightPower), random.randint(0, self.lightPower), random.randint(0, self.lightPower))
        self.np.setColor(2, random.randint(0, self.lightPower), random.randint(0, self.lightPower), random.randint(0, self.lightPower))
        left = random.randint(0, 2)
        right = random.randint(0, 2)
        if (left == 0): self.earLeft.stop()
        elif (left == 1): self.earLeft.forward(random.random() / 2)
        elif (left == 2): self.earLeft.backward(random.random() / 2)
        if (right == 0): self.earRight.stop()
        elif (right == 1): self.earRight.forward(random.random() / 2)
        elif (right == 2): self.earRight.backward(random.random() / 2)

    def stop(self):
        self.earLeft.stop()
        self.earRight.stop()
        self.np.setColor(0, 0, 0, 0)
        self.np.setColor(1, 0, 0, 0)
        self.np.setColor(2, 0, 0, 0)