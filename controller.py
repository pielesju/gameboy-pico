'''
    PiBoy Controller
    13.09.2022 Julian Pieles
'''

from button import Button

class Controller:
    def __init__(self):
        self.DEBOUNCE_DURATION = 100

        self.button_up = Button(16)
        self.button_down = Button(19)
        self.button_left = Button(18)
        self.button_right = Button(15)
        
    def on_up(self, callback):
        self.button_up.on_press(callback)

    def on_down(self, callback):
        self.button_down.on_press(callback)

    def on_left(self, callback):
        self.button_left.on_press(callback)

    def on_right(self, callback):
        self.button_right.on_press(callback)


if __name__ == "__main__":
    ctrl = Controller()
    ctrl.on_up(lambda btn: print('up'))
    ctrl.on_down(lambda btn: print('down'))
    ctrl.on_left(lambda btn: print('left'))
    ctrl.on_right(lambda btn: print('right'))

