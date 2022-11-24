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