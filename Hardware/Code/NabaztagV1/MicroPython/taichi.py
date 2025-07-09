from time import sleep
import _thread
import random

class TAICHI:
    def __init__(self, np, earLeft, earRight, lightPower):
        self.np = np
        self.earLeft = earLeft
        self.earRight = earRight
        self.lightPower = lightPower
        self.animation = False
        random.seed()

    def go(self):
        if self.animation == False:
            self.animation = True
            _thread.start_new_thread(self._move, ())

    def _move(self):
        while self.animation:
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
            sleep(1)

    def stop(self):
        if self.animation == True:
            self.animation = False
            self.earLeft.stop()
            self.earRight.stop()
            self.np.setColor(0, 0, 0, 0)
            self.np.setColor(1, 0, 0, 0)
            self.np.setColor(2, 0, 0, 0)
            sleep(1)
