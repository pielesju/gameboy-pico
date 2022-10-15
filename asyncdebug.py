
import time
from button import Button
from machine import Timer, Pin
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
        self.led = Pin("LED", Pin.OUT)

    def draw(self, direction):
        state = direction
        for x in range(8):
            for y in range(8):
                if state[x][y] != 0:
                    display.pixel(x, y, 1)
                else:
                    display.pixel(x, y, 0)
    
    def loop(self, t):
        self.led.toggle()

        #last press
        lp = self.controller.last_button_pressed
        
        print('last_press: ', lp)
        
        if (lp == 'up'): self.draw(self.up)
        elif (lp == 'down'): self.draw(self.down)
        elif (lp == 'left'): self.draw(self.left)
        elif (lp == 'right'): self.draw(self.right)
        else: self.draw(self.empty)
        
        display.show()
        self.controller.reset_press()
    
    def run(self):
        game_loop_timer = Timer()
        game_loop_timer.init(mode=Timer.PERIODIC, period=500, callback=self.loop)

        # led_timer = Timer()
        # led_timer.init(mode=Timer.PERIODIC, period=250, callback=lambda t:led.toggle())

        
if __name__ == "__main__":
    game = AsyncDebug()
    game.run()