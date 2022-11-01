'''
    PiBoy Controller
    13.09.2022 Julian Pieles
'''

from button import Button

class Controller:
    def __init__(self):
        self.button_up = Button(16)
        self.button_down = Button(19)
        self.button_left = Button(18)
        self.button_right = Button(15)
        self.button_a = Button(11)
        self.button_b = Button(9)

    def on_up(self, callback):
        self.button_up.on_press(callback)

    def on_down(self, callback):
        self.button_down.on_press(callback)

    def on_left(self, callback):
        self.button_left.on_press(callback)

    def on_right(self, callback):
        self.button_right.on_press(callback)

    def on_a(self, callback):
        self.button_a.on_press(callback)

    def on_b(self, callback):
        self.button_b.on_press(callback)

if __name__ == "__main__":
    ctrl = Controller()
    ctrl.on_up(lambda btn: print('up'))
    ctrl.on_down(lambda btn: print('down'))
    ctrl.on_left(lambda btn: print('left'))
    ctrl.on_right(lambda btn: print('right'))
    ctrl.on_a(lambda btn: print('a'))
    ctrl.on_b(lambda btn: print('b'))