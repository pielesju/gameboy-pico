import machine
import time
from button import Button
from game import Game
from machine import Timer, Pin
from display import Display
from controller import Controller



class Tetris(Game):
    def __init__(self, display, controller, menu):
        Game.__init__(self, display, controller, menu) # pass parameters into parent class

        self.lastButtonPressed = None


    def loop(self, t):
        self.led.toggle()

    def run(self):
        def up_fn(btn_pressed):    self.lastButtonPressed = 'up'
        def down_fn(btn_pressed):  self.lastButtonPressed = 'down'
        def left_fn(btn_pressed):  self.lastButtonPressed = 'left'
        def right_fn(btn_pressed): self.lastButtonPressed = 'right'
        def a_fn(btn_pressed):     self.lastButtonPressed = 'a'
        def b_fn(btn_pressed):     self.exit()

        self.controller.on_up(up_fn)
        self.controller.on_down(down_fn)
        self.controller.on_left(left_fn)
        self.controller.on_right(right_fn)
        self.controller.on_a(a_fn)
        self.controller.on_b(b_fn)

        self.gameLoop.init(mode=Timer.PERIODIC, period=1000, callback=self.loop)
















