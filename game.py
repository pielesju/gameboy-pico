

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
        self.menu.stop_running_game()

    def addStates(self, args):

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