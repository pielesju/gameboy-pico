from machine import Pin
import time

class Button:

    def __init__(self, pin_no, callback):
        self.pin_no = pin_no
        self.pressed = False
        self.btn = Pin(self.pin_no, Pin.IN, Pin.PULL_DOWN)
        self.btn.irq(trigger=Pin.IRQ_FALLING, handler=callback)
        
    def is_pressed(self):
        return self.pressed
    
    def clear(self):
        self.pressed = False

if __name__ == "__main__":
   btn = Button(16)
