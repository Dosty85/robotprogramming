from neopixel import NeoPixel
from microbit import pin0
from microbit import sleep

class Robot:
    def __init__(self):
        self.np = NeoPixel(pin0, 8)
        self.COLOR_RED = (60, 0, 0)
        self.COLOR_RED_MAX = (255, 0, 0)
        self.COLOR_WHITE = (255, 255, 255)
        self.COLOR_YELLOW = (247, 247, 1)
        self.COLOR_BLACK = (0, 0, 0)

        self.vypni_svetla()

    def indikuj(self, smer_zataceni):
        led1 = None
        led2 = None
        if smer_zataceni == "doprava":
            led1 = 1
            led2 = 7
        elif smer_zataceni == "doleva":
            led1 = 3
            led2 = 4
        if(led1 is not None):
            for i in range(0,3):
                self.np[led1] = self.COLOR_YELLOW
                self.np[led2] = self.COLOR_YELLOW
                self.np.write()
                sleep(500)
                self.np[led1] = self.COLOR_BLACK
                self.np[led2] = self.COLOR_BLACK
                self.np.write()
                sleep(500)

    def zapni_svetla(self):
        self.np[1] = self.COLOR_WHITE
        self.np[2] = self.COLOR_WHITE
        self.np[5] = self.COLOR_RED
        self.np[6] = self.COLOR_RED
        self.np.write()


    def brzdi(self):
        self.np[5] = self.COLOR_RED_MAX
        self.np[6] = self.COLOR_RED_MAX
        self.np.write()

    def vypni_svetla(self):
        for i in range(0, 8):
            self.np[i] = self.COLOR_BLACK
        self.np.write()

robot = Robot()
robot.zapni_svetla()
sleep(1000)
robot.brzdi()
sleep(1000)
robot.vypni_svetla()
sleep(1000)
robot.indikuj("doprava")
sleep(1000)
robot.indikuj("doleva")
