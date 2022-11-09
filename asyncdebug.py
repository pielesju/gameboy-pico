import machine
import time
from button import Button
from game import Game
from machine import Timer, Pin
from display import Display
from controller import Controller

class AsyncDebug(Game):
    def __init__(self, display, controller, menu):
        Game.__init__(self, display, controller, menu) # pass parameters into parent class

        self.lastButtonPressed = None

        self.up_image = [
            [0,0,0,1,1,0,0,0],
            [0,0,1,1,1,1,0,0],
            [0,1,1,1,1,1,1,0],
            [1,1,0,1,1,0,1,1],
            [1,0,0,1,1,0,0,1],
            [0,0,0,1,1,0,0,0],
            [0,0,0,1,1,0,0,0],
            [0,0,0,1,1,0,0,0]
        ]
        self.down_image = [
            [0,0,0,1,1,0,0,0],
            [0,0,0,1,1,0,0,0],
            [0,0,0,1,1,0,0,0],
            [1,0,0,1,1,0,0,1],
            [1,1,0,1,1,0,1,1],
            [0,1,1,1,1,1,1,0],
            [0,0,1,1,1,1,0,0],
            [0,0,0,1,1,0,0,0]
        ]
        self.left_image = [
            [0,0,0,1,1,0,0,0],
            [0,0,1,1,0,0,0,0],
            [0,1,1,0,0,0,0,0],
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1],
            [0,1,1,0,0,0,0,0],
            [0,0,1,1,0,0,0,0],
            [0,0,0,1,1,0,0,0]
        ]
        self.right_image = [
            [0,0,0,1,1,0,0,0],
            [0,0,0,0,1,1,0,0],
            [0,0,0,0,0,1,1,0],
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1],
            [0,0,0,0,0,1,1,0],
            [0,0,0,0,1,1,0,0],
            [0,0,0,1,1,0,0,0]
        ]
        self.empty = [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]
        ]

    def loop(self, t):
        self.led.toggle()
        #last press
        lp = self.lastButtonPressed

        print('last_press: ', lp)

        if (lp == 'up'): self.draw(self.up_image)
        elif (lp == 'down'): self.draw(self.down_image)
        elif (lp == 'left'): self.draw(self.left_image)
        elif (lp == 'right'): self.draw(self.right_image)
        else: self.draw(self.empty)

        self.lastButtonPressed = None

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

if __name__ == "__main__":
    display = Display()
    controller = Controller()
    menu = Menu(display, controller)

    game = AsyncDebug(display, controller, menu)
    game.run()


















