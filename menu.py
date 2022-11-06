from display import Display
from controller import Controller
from machine import Timer


from asyncdebug import AsyncDebug
from snake import SnakeGame
from stackgame import StackGame
from paint import PaintGame


class Menu:
    def __init__(self, display, controller):
        self.display = display
        self.controller = controller
        
        self.runningGame = None

        self.index = 0
        self.entries = [
            "AsyncDebug",
            "SnakeGame",
            "StackGame",
            "Paint"
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
        if  self.entries[self.index] == 'AsyncDebug':
            self.runningGame = AsyncDebug(self.display, self.controller, self)
        elif self.entries[self.index] == 'SnakeGame':
            self.runningGame = SnakeGame(self.display, self.controller, self)
        elif self.entries[self.index] == 'StackGame':
            self.runningGame = StackGame(self.display, self.controller, self)
        elif self.entries[self.index] == 'Paint':
            self.runningGame = PaintGame(self.display, self.controller, self)
        else:
            raise Exception('select_entry() fail')

        print(self.runningGame)
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
        print(self.index+1)
        self.display.showtext(str(self.index+1), 0, 1)

if __name__ == "__main__":
    menu = Menu(Display(), Controller())
    menu.run()