
import time
from button import Button
from machine import Timer
from display import Display
from controller import Controller

display = Display()

class AsyncDebug:
    def __init__(self):
        self.controller = Controller()
        self.up = [
            [0,0,0,1,1,0,0,0],
            [0,0,1,1,1,1,0,0],
            [0,1,1,1,1,1,1,0],
            [1,1,0,1,1,0,1,1],
            [1,0,0,1,1,0,0,1],
            [0,0,0,1,1,0,0,0],
            [0,0,0,1,1,0,0,0],
            [0,0,0,1,1,0,0,0]
        ]
        self.down = [
            [0,0,0,1,1,0,0,0],
            [0,0,0,1,1,0,0,0],
            [0,0,0,1,1,0,0,0],
            [1,0,0,1,1,0,0,1],
            [1,1,0,1,1,0,1,1],
            [0,1,1,1,1,1,1,0],
            [0,0,1,1,1,1,0,0],
            [0,0,0,1,1,0,0,0]
        ]
        self.left = [
            [0,0,0,1,1,0,0,0],
            [0,0,1,1,0,0,0,0],
            [0,1,1,0,0,0,0,0],
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1],
            [0,1,1,0,0,0,0,0],
            [0,0,1,1,0,0,0,0],
            [0,0,0,1,1,0,0,0]
        ]
        self.right = [
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
        for x in range(8):
            for y in range(8):
                if state[x][y] != 0:
                    display.pixel(x, y, 1)
                else:
                    display.pixel(x, y, 0)
    
    def loop(self, t):
        display.pixel(0,0,1)
        display.show()
        time.sleep_ms(200)
        display.pixel(0,0,0)
        display.show()
        print(self.controller.last_button_pressed)
        if (self.controller.last_button_pressed == 'up'):
            self.draw(self.up)
        elif (self.controller.last_button_pressed == 'down'):
            self.draw(self.down)
        elif (self.controller.last_button_pressed == 'left'):
            self.draw(self.left)
        elif (self.controller.last_button_pressed == 'right'):
            self.draw(self.right)
        else:
            self.draw(self.empty)
            print('none')
        
        display.show()
        self.controller.reset_press()
    
    def run(self):
        timer = Timer()
        timer.init(mode=Timer.PERIODIC, period=500, callback=self.loop)
