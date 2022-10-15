'''
    PiBoy Controller
    13.09.2022 Julian Pieles
'''

from button import Button
from machine import Timer
from machine import Pin

class Controller:
    def __init__(self):
        self.button_up = Pin(16, Pin.IN, Pin.PULL_DOWN)
        self.button_down = Pin(18, Pin.IN, Pin.PULL_DOWN)
        self.button_left = Pin(17, Pin.IN, Pin.PULL_DOWN)
        self.button_right = Pin(19, Pin.IN, Pin.PULL_DOWN)
        
        self.button_up.irq(trigger=Pin.IRQ_FALLING, handler=self.handle_press)
        self.button_down.irq(trigger=Pin.IRQ_FALLING, handler=self.handle_press)
        self.button_left.irq(trigger=Pin.IRQ_FALLING, handler=self.handle_press)
        self.button_right.irq(trigger=Pin.IRQ_FALLING, handler=self.handle_press)
        
        self.last_button_pressed = None
        
    def handle_press(self, btn_pressed):
        print("Interrupt has occured: ", end='')
        if (btn_pressed == self.button_up):
            self.last_button_pressed = 'up'
            print('up')
        elif (btn_pressed == self.button_down):
            self.last_button_pressed = 'down'
            print('down')
        elif (btn_pressed == self.button_left):
            self.last_button_pressed = 'left'
            print('left')
        elif (btn_pressed == self.button_right):
            self.last_button_pressed = 'right'
            print('right')

    def reset_press(self): #should be "reset_last_button_pressed()"
        self.last_button_pressed = None

if __name__ == "__main__":
   ctrl = Controller()
