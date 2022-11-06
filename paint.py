from display import Display
from controller import Controller
from machine import Timer, Pin
import machine
import time
import framebuf

class Canvas:
    def __init__(self):
        self.state = [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
        ]

    def set_pixel(self, brush):
        self.state[brush.y][brush.x] = 1

    def unset_pixel(self, brush):
        self.state[brush.y][brush.x] = 0

    def toggle_pixel(self, brush):
        self.state[brush.y][brush.x] = self.state[brush.y][brush.x] ^ 1

class Brush:
    def __init__(self):
        self.x = 4
        self.y = 4

    def move_up(self):
        self.y -= 1
        if self.y < 0:
            self.y = 7

    def move_down(self):
        self.y += 1
        if self.y > 7:
            self.y = 0

    def move_left(self):
        self.x -= 1
        if self.x < 0:
            self.x = 7

    def move_right(self):
        self.x += 1
        if self.x > 7:
            self.x = 0

class PaintGame:
    def __init__(self, display, controller, menu):
        self.display = display
        self.controller = controller
        self.menu = menu
        self.led = Pin(25, Pin.OUT)
        self.canvas = Canvas()
        self.brush = Brush()
        self.blinkTimer = Timer()
        self.movedLastTick = False

    def move(self, direction):
        if direction == 'up':
            self.brush.move_up()
        elif direction == 'down':
            self.brush.move_down()
        elif direction == 'left':
            self.brush.move_left()
        elif direction == 'right':
            self.brush.move_right()
        else:
            return
        self.movedLastTick = True

    def draw(self, state):
        for y in range(8):
            for x in range(8):
                try:
                    self.display.pixel(x, y, state[y][x]) # withuot -x+7 the game will be upside down
                except IndexError:
                    self.display.pixel(x, y, 0)
        self.display.show()

    def blink(self, t):
        self.display.toggle_pixel(self.brush.x, self.brush.y)
        if self.movedLastTick:
            self.draw(self.canvas.state)
            self.movedLastTick = False

    def exit(self):
        self.blinkTimer.deinit()
        self.menu.stop_running_game()

    def run(self):
        print('starting paint')

        def up_fn(btn_pressed):    self.move('up')
        def down_fn(btn_pressed):  self.move('down')
        def left_fn(btn_pressed):  self.move('left')
        def right_fn(btn_pressed): self.move('right')
        def b_fn(btn_pressed):     self.exit()
        def a_fn(btn_pressed):
            print('a')
            self.canvas.toggle_pixel(self.brush)
            self.draw(self.canvas.state)

        self.controller.on_up(up_fn)
        self.controller.on_down(down_fn)
        self.controller.on_left(left_fn)
        self.controller.on_right(right_fn)
        self.controller.on_a(a_fn)
        self.controller.on_b(b_fn)

        self.display.fill(0)
        self.display.show()

        self.blinkTimer.init(mode=Timer.PERIODIC,
                              period=250,
                              callback=self.blink)

if __name__ == "__main__":
    game = PaintGame(Display(), Controller())
    game.run()


