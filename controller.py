"""
    GameBoy Pico Controller
    13.09.2022 Julian Pieles
"""

from machine import Pin

class Controller:

    def __init__(self):
        self.button_up = Pin(15, Pin.IN)
        self.button_down = Pin(12, Pin.IN)
        self.button_left = Pin(14, Pin.IN)
        self.button_right = Pin(13, Pin.IN)

    def up(self):
        return self.button_up.value()

    def down(self):
        return self.button_down.value()

    def left(self):
        return self.button_left.value()

    def right(self):
        return self.button_right.value()