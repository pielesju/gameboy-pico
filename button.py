#  dP                  dP     dP
#  88                  88     88
#  88d888b. dP    dP d8888P d8888P .d8888b. 88d888b.    88d888b. dP    dP
#  88'  `88 88    88   88     88   88'  `88 88'  `88    88'  `88 88    88
#  88.  .88 88.  .88   88     88   88.  .88 88    88 dP 88.  .88 88.  .88
#  88Y8888' `88888P'   dP     dP   `88888P' dP    dP 88 88Y888P' `8888P88
#                                                       88            .88
#                                                       dP        d8888P

from machine import Pin
from machine import Timer

class Button:

    def __init__(self, pin_no):
        self.DEBOUNCE_DURATION = 100

        self.button = Pin(pin_no, Pin.IN, Pin.PULL_DOWN)
        self.debounce_timer = Timer()
        self.is_debounce_active = False

        self.button.irq(trigger=Pin.IRQ_FALLING, handler=self.callback_wrapper)

        self.callback = None

    def on_press(self, callback): # The callback NEEDS to take one parameter. For example callback(btn_pressed)
        self.callback = callback
        # it's not enough to just redefine callback_up,the whole ISR needs to be redefined.
        self.button.irq(trigger=Pin.IRQ_FALLING, handler=self.callback_wrapper)

    def callback_wrapper(self, btn_pressed):
        if self.is_debounce_active:
            print(".", end='')
            return

        def reset_debounce(t): self.is_debounce_active = False
        self.debounce_timer.init(mode=Timer.ONE_SHOT, period=self.DEBOUNCE_DURATION, callback=reset_debounce)

        self.is_debounce_active = True

        if self.callback == None:
            print('No callback for "' + str(btn_pressed) + '" defined.')
            return

        self.callback(btn_pressed)

    def clear(self):
        self.pressed = False

if __name__ == "__main__":
    button_up = Button(15)
    button_down = Button(8)
    button_left = Button(10)
    button_right = Button(13)
    button_a = Button(11)
    button_b = Button(9)

    button_up.on_press(lambda x: print ('up'))
    button_down.on_press(lambda x: print ('down'))
    button_left.on_press(lambda x: print ('left'))
    button_right.on_press(lambda x: print ('right'))
    button_a.on_press(lambda x: print ('a'))
    button_b.on_press(lambda x: print ('b'))