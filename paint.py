from display import Display
from controller import Controller
from machine import Timer, Pin
import machine
import time
import framebuf

class Canvas:
    def __init__(self):
        pass

class Brush:
    def __init__(self):
        pass

class PaintGame:
    def __init__(self, display, controller):
        self.display = display
        self.controller = controller
        self.led = Pin(25, Pin.OUT)
        self.canvas = Canvas()
        self.brush = Brush()
        self.tower_height = 0
        self.tower_height_offset = 0

    def draw(self, state):
        for y in range(8):
            for x in range(8):
                try:
                    self.display.pixel(y, -x+7, state[x][y]) # withuot -x+7 the game will be upside down
                except IndexError:
                    self.display.pixel(y, -x+7, 0)
        self.display.show()

    def lose(self):
        pass

    def run(self):
        print('starting stack')

        def up_fn(btn_pressed):    print('up')
        def down_fn(btn_pressed):  print('down')
        def left_fn(btn_pressed):  print('left')
        def right_fn(btn_pressed): print('right')
        def a_fn(btn_pressed):     print('a')
        def b_fn(btn_pressed):     machine.reset()

        self.controller.on_up(up_fn)
        self.controller.on_down(down_fn)
        self.controller.on_left(left_fn)
        self.controller.on_right(right_fn)
        self.controller.on_a(a_fn)
        self.controller.on_b(b_fn)

        self.display.fill(0)
        self.display.show()

        buffer = bytearray(b'.\xf0\xf1\xf2\xf2\xf2\xf2\xf2\xf2')
        fb = framebuf.FrameBuffer(buffer, 8, 8,framebuf.MONO_HLSB)
        self.display.blit(fb,0,0)
        self.display.show()

if __name__ == "__main__":
    game = PaintGame(Display(), Controller())
    game.run()


