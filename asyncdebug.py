import machine
import time
from button import Button
from machine import Timer, Pin
from display import Display
from controller import Controller

class AsyncDebug:
    def __init__(self, display, controller, menu):
        self.display = display
        self.controller = controller
        self.menu = menu
        self.gameLoopTimer = Timer()
        self.led = Pin(25, Pin.OUT)
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


    def draw(self, direction):
        state = direction
        for y in range(8):
            for x in range(8):
                if state[y][x] != 0:
                    self.display.pixel(x, y, 1)
                else:
                    self.display.pixel(x, y, 0)
        self.display.show()

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

    def exit(self):
        self.gameLoopTimer.deinit()
        self.menu.stop_running_game()

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

        self.gameLoopTimer.init(mode=Timer.PERIODIC, period=1000, callback=self.loop)

        # led_timer = Timer()
        # led_timer.init(mode=Timer.PERIODIC, period=250, callback=lambda t:led.toggle())


if __name__ == "__main__":
    game = AsyncDebug()
    game.run()