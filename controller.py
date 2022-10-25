'''
    PiBoy Controller
    13.09.2022 Julian Pieles
'''

from button import Button
from machine import Timer
from machine import Pin

class Controller:
    def __init__(self):
        self.DEBOUNCE_DURATION = 100

        self.button_up = Pin(16, Pin.IN, Pin.PULL_DOWN)
        self.button_down = Pin(18, Pin.IN, Pin.PULL_DOWN)
        self.button_left = Pin(17, Pin.IN, Pin.PULL_DOWN)
        self.button_right = Pin(19, Pin.IN, Pin.PULL_DOWN)

        self.debounce_up_timer = Timer()
        self.debounce_down_timer = Timer()
        self.debounce_left_timer = Timer()
        self.debounce_right_timer = Timer()
        
        self.is_debounce_up_active = False
        self.is_debounce_down_active = False
        self.is_debounce_left_active = False
        self.is_debounce_right_active = False
    
        self.button_up.irq(trigger=Pin.IRQ_FALLING, handler=self.callback_up_wrapper)
        self.button_down.irq(trigger=Pin.IRQ_FALLING, handler=self.callback_down_wrapper)
        self.button_left.irq(trigger=Pin.IRQ_FALLING, handler=self.callback_left_wrapper)
        self.button_right.irq(trigger=Pin.IRQ_FALLING, handler=self.callback_right_wrapper)
                
        self.callback_up = None        
        self.callback_down = None
        self.callback_left = None
        self.callback_right = None
    
    def on_up(self, callback): # The callback NEEDS to take one parameter. For example callback(btn_pressed)
        self.callback_up = callback
        # it's not enough to just redefine callback_up,the whole ISR needs to be redefined.
        self.button_up.irq(trigger=Pin.IRQ_FALLING, handler=self.callback_up_wrapper)

    def on_down(self, callback):
        self.callback_down = callback
        # it's not enough to just redefine callback_down,the whole ISR needs to be redefined.
        self.button_down.irq(trigger=Pin.IRQ_FALLING, handler=self.callback_down_wrapper)

    def on_left(self, callback):
        self.callback_left = callback
        # it's not enough to just redefine callback_left,the whole ISR needs to be redefined.
        self.button_left.irq(trigger=Pin.IRQ_FALLING, handler=self.callback_left_wrapper)

    def on_right(self, callback):
        self.callback_right = callback
        # it's not enough to just redefine callback_right,the whole ISR needs to be redefined.
        self.button_right.irq(trigger=Pin.IRQ_FALLING, handler=self.callback_right_wrapper)

    def callback_up_wrapper(self, btn_pressed):
        if self.is_debounce_up_active:
            print(".", end='')
            return

        def reset_debounce(t): self.is_debounce_up_active = False
        self.debounce_up_timer.init(mode=Timer.ONE_SHOT, period=self.DEBOUNCE_DURATION, callback=reset_debounce)

        self.is_debounce_up_active = True
        
        if self.callback_up == None:
            print('No callback for "up" defined.')
            return

        self.callback_up(btn_pressed)

    def callback_down_wrapper(self, btn_pressed):
        if self.is_debounce_down_active:
            print(".", end='')
            return
            
        def reset_debounce(t): self.is_debounce_down_active = False
        self.debounce_down_timer.init(mode=Timer.ONE_SHOT, period=self.DEBOUNCE_DURATION, callback=reset_debounce)

        self.is_debounce_down_active = True
        
        if self.callback_down == None:
            print('No callback for "up" defined.')
            return

        self.callback_down(btn_pressed)

    def callback_left_wrapper(self, btn_pressed):
        if self.is_debounce_left_active:
            print(".", end='')
            return
            
        def reset_debounce(t): self.is_debounce_left_active = False
        self.debounce_left_timer.init(mode=Timer.ONE_SHOT, period=self.DEBOUNCE_DURATION, callback=reset_debounce)

        self.is_debounce_left_active = True
        
        if self.callback_left == None:
            print('No callback for "up" defined.')
            return

        self.callback_left(btn_pressed)

    def callback_right_wrapper(self, btn_pressed):
        if self.is_debounce_right_active:
            print(".", end='')
            return
            
        def reset_debounce(t): self.is_debounce_right_active = False
        self.debounce_right_timer.init(mode=Timer.ONE_SHOT, period=self.DEBOUNCE_DURATION, callback=reset_debounce)

        self.is_debounce_right_active = True
        
        if self.callback_right == None:
            print('No callback for "up" defined.')
            return

        self.callback_right(btn_pressed)

if __name__ == "__main__":
    ctrl = Controller()
    ctrl.on_up(lambda btn: print(btn))
    ctrl.on_down(lambda btn: print(btn))
    ctrl.on_left(lambda btn: print(btn))
    ctrl.on_right(lambda btn: print(btn))