

#
#
#  88d8b.d8b. .d8888b. 88d888b. dP    dP    88d888b. dP    dP
#  88'`88'`88 88ooood8 88'  `88 88    88    88'  `88 88    88
#  88  88  88 88.  ... 88    88 88.  .88 dP 88.  .88 88.  .88
#  dP  dP  dP `88888P' dP    dP `88888P' 88 88Y888P' `8888P88
#                                           88            .88
#                                           dP        d8888P

from display import Display
from controller import Controller
from machine import Timer
from debuggame import DebugGame
from snakegame import SnakeGame
from stackgame import StackGame
from paintgame import PaintGame

class Menu:
    def __init__(self, display, controller):
        self.display = display
        self.controller = controller

        self.runningGame = None

        self.index = 0
        self.entries = [
            "DebugGame",
            "SnakeGame",
            "StackGame",
            "PaintGame"
        ]

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
        if (self.entries[self.index] == 'DebugGame'):
            self.runningGame = DebugGame(self.display, self.controller, self)
        elif (self.entries[self.index] == 'SnakeGame'):
            self.runningGame = SnakeGame(self.display, self.controller, self)
        elif (self.entries[self.index] == 'StackGame'):
            self.runningGame = StackGame(self.display, self.controller, self)
        elif (self.entries[self.index] == 'PaintGame'):
            self.runningGame = PaintGame(self.display, self.controller, self)
        else:
            raise Exception('select_entry() fail')

        self.runningGame.run()

    def stop_running_game(self):
        del self.runningGame
        self.runningGame = None
        self.run()

    def run(self):
        def up_fn(btn_pressed): print('up')
        def down_fn(btn_pressed): print('down')
        def left_fn(btn_pressed): self.previous_entry()
        def right_fn(btn_pressed): self.next_entry()
        def a_fn(btn_pressed): self.select_entry()
        def b_fn(btn_pressed): print('b')

        self.controller.on_up(up_fn)
        self.controller.on_down(down_fn)
        self.controller.on_left(left_fn)
        self.controller.on_right(right_fn)
        self.controller.on_a(a_fn)
        self.controller.on_b(b_fn)

        self.display.showtext(str(self.index+1), 0, 1)