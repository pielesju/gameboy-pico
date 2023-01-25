#                               dP                     dP dP
#                               88                     88 88
#  .d8888b. .d8888b. 88d888b. d8888P 88d888b. .d8888b. 88 88 .d8888b. 88d888b.    88d888b. dP    dP
#  88'  `"" 88'  `88 88'  `88   88   88'  `88 88'  `88 88 88 88ooood8 88'  `88    88'  `88 88    88
#  88.  ... 88.  .88 88    88   88   88       88.  .88 88 88 88.  ... 88       dP 88.  .88 88.  .88
#  `88888P' `88888P' dP    dP   dP   dP       `88888P' dP dP `88888P' dP       88 88Y888P' `8888P88
#                                                                                 88            .88
#                                                                                 dP        d8888P

'''
    PiBoy Controller
    13.09.2022 Julian Pieles
'''

from button import Button

class Controller:
    def __init__(self):
        self.button_up = Button(15)
        self.button_down = Button(8)
        self.button_left = Button(10)
        self.button_right = Button(13)
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