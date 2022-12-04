

#
#
#  .d8888b. .d8888b. 88d8b.d8b. .d8888b.    88d888b. dP    dP
#  88'  `88 88'  `88 88'`88'`88 88ooood8    88'  `88 88    88
#  88.  .88 88.  .88 88  88  88 88.  ... dP 88.  .88 88.  .88
#  `8888P88 `88888P8 dP  dP  dP `88888P' 88 88Y888P' `8888P88
#       .88                                 88            .88
#   d8888P                                  dP        d8888P

from display import Display
from controller import Controller
from machine import Timer, Pin
import machine
import time

class Game:
    def __init__(self, display, controller, menu):
        self.display = display
        self.controller = controller
        self.menu = menu
        self.led = Pin(25, Pin.OUT)
        self.gameLoop = Timer()
        self.scoreLoop = Timer()

    def draw(self, state):
        for y in range(8):
            for x in range(8):
                try:
                    self.display.pixel(x, y, state[y][x])
                except IndexError:
                    self.display.pixel(x, y, 0)
        self.display.show()

    def exit(self):
        self.gameLoop.deinit()
        self.scoreLoop.deinit()
        self.menu.stop_running_game()

    def add_states(self, args):
        union = [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]
        ]

        for z in range(len(args)):
            for y in range(8):
                for x in range(8):
                    union[y][x] = args[z][y][x] or union[y][x]

        return union

    def die_animation(self, state):
        self.display.fill(1)
        self.display.show()
        time.sleep_ms(100)

        self.draw(state)
        time.sleep_ms(100)

        self.display.fill(1)
        self.display.show()
        time.sleep_ms(100)

        self.draw(state)
        time.sleep_ms(100)

        self.display.fill(1)
        self.display.show()
        time.sleep_ms(100)

        self.draw(state)

    def score_animation(self, score, state):
        self.strScore = str(score)
        self.index = 0

        def loop(t):
            if self.index < len(self.strScore):
                self.display.showtext(self.strScore[self.index], 0,1)
                self.index = self.index + 1
            else:
                self.draw(state)
                self.index = 0

        self.scoreLoop.init(mode=Timer.PERIODIC,
                            period=800,
                            callback=loop)