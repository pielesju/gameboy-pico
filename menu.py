from display import Display
from controller import Controller
from machine import Timer
import time

class Menu:
    def __init__(self, display, controller, games):
        self.display = display
        self.controller = controller

        self.index = 0
        self.entries = games

    def next_entry(self):
        self.index += 1
        if self.index >= len(self.entries):
            self.index = 0
        self.display.showtext(str(self.index+1), 0, 1)
    
    def previous_entry(self):
        self.index -= 1
        if self.index < 0:
            self.index = len(self.entries)-1
        self.display.showtext(str(self.index+1), 0, 1)

    def select_entry(self):
        self.entries[self.index].run()

    def run(self):
        def up_fn(btn_pressed): print('up')
        def down_fn(btn_pressed): self.select_entry()
        def left_fn(btn_pressed): self.previous_entry()
        def right_fn(btn_pressed): self.next_entry()

        self.controller.on_up(up_fn)
        self.controller.on_down(down_fn)
        self.controller.on_left(left_fn)
        self.controller.on_right(right_fn)

        self.display.showtext(str(self.index+1), 0, 1)

if __name__ == "__main__":
    menu = Menu(Display(), Controller())
    menu.run()