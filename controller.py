'''
    PiBoy Controller
    13.09.2022 Julian Pieles
'''

from button import Button

class Controller:

    def __init__(self):
        self.button_up = Button(16)
        self.button_down = Button(18)
        self.button_left = Button(17)
        self.button_right = Button(19)

    def up(self):
        return self.button_up.is_pressed()

    def down(self):
        return self.button_down.is_pressed()

    def left(self):
        return self.button_left.is_pressed()

    def right(self):
        return self.button_right.is_pressed()