#        dP          dP
#        88          88
#  .d888b88 .d8888b. 88d888b. dP    dP .d8888b. .d8888b. .d8888b. 88d8b.d8b. .d8888b.    88d888b. dP    dP
#  88'  `88 88ooood8 88'  `88 88    88 88'  `88 88'  `88 88'  `88 88'`88'`88 88ooood8    88'  `88 88    88
#  88.  .88 88.  ... 88.  .88 88.  .88 88.  .88 88.  .88 88.  .88 88  88  88 88.  ... dP 88.  .88 88.  .88
#  `88888P8 `88888P' 88Y8888' `88888P' `8888P88 `8888P88 `88888P8 dP  dP  dP `88888P' 88 88Y888P' `8888P88
#                                           .88      .88                                 88            .88
#                                       d8888P   d8888P                                  dP        d8888P

from machine import Timer
from game import Game

class DebugGame(Game):
    def __init__(self, display, controller, menu):
        Game.__init__(self, display, controller, menu) # pass parameters into parent class

        self.LOOP_SPEED = 800
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
        print('last_press: ', self.lastButtonPressed)

        if   (self.lastButtonPressed == 'up'   ): self.draw(self.up_image)
        elif (self.lastButtonPressed == 'down' ): self.draw(self.down_image)
        elif (self.lastButtonPressed == 'left' ): self.draw(self.left_image)
        elif (self.lastButtonPressed == 'right'): self.draw(self.right_image)
        else: self.draw(self.empty)

        self.lastButtonPressed = None

    def run(self):
        def up_fn(btn_pressed):    self.lastButtonPressed = 'up'
        def down_fn(btn_pressed):  self.lastButtonPressed = 'down'
        def left_fn(btn_pressed):  self.lastButtonPressed = 'left'
        def right_fn(btn_pressed): self.lastButtonPressed = 'right'
        def a_fn(btn_pressed):     self.lastButtonPressed = 'a'
        def b_fn(btn_pressed):     self.exit() # from Game()

        self.controller.on_up(up_fn)
        self.controller.on_down(down_fn)
        self.controller.on_left(left_fn)
        self.controller.on_right(right_fn)
        self.controller.on_a(a_fn)
        self.controller.on_b(b_fn)

        self.gameLoop.init(mode=Timer.PERIODIC,
                           period=self.LOOP_SPEED,
                           callback=self.loop)