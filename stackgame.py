from machine import Timer
from game import Game
import time

class Board:
    def __init__(self):
        self.fullState = []
        self.towerHeight = 0
        self.towerHeightOffset = 0

    def add_row(self, row):
        self.fullState.append(row)

        self.towerHeight += 1
        if self.towerHeight >= 7:
            self.towerHeightOffset += 1

    @property
    def state(self):
        section = self.fullState[self.towerHeightOffset:self.towerHeight]
        section.extend([[0,0,0,0,0,0,0,0]]*8)
        state = section[0:8]
        state.reverse()
        return state

    def debug_print(self):
        print("\x1B\x5B2J", end="")
        print("\x1B\x5BH", end="")
        print(self.fullState)
        for y in range(8):
            for x in range(8):
                try:
                    print(self.state[y][x], end='')
                except IndexError:
                    print('0', end='')
            print('')
        print('')

class Row:
    def __init__(self):
        self.state = [0,0,0,0,1,1,1,1]
        self.direction = 'left' #one of 'left' or 'right'

    def move_left(self):
        self.state.append(self.state.pop(0))

    def move_right(self):
        self.state.insert(0,self.state.pop())

    def move(self):
        LEFTMOST_INDEX = 0
        RIGHTMOST_INDEX = 7

        if self.direction == 'left' and self.state[LEFTMOST_INDEX] == 1:
            self.direction = 'right'

        elif self.direction == 'right' and self.state[RIGHTMOST_INDEX] == 1:
            self.direction = 'left'

        if self.direction == 'left':
            self.move_left()
        elif self.direction == 'right':
            self.move_right()
        else:
            raise Exception("couldn't decide to move left or right")

class StackGame(Game):
    def __init__(self, display, controller, menu):
        Game.__init__(self, display, controller, menu) # pass parameters into parent class
        self.board = Board()
        self.row = Row()
        self.LOOP_SPEED = 400

    @property
    def state(self):
        bottom_padding = self.board.towerHeight - self.board.towerHeightOffset
        top_padding = 7 - bottom_padding
        return self.add_states([
            self.board.state,
            [[0,0,0,0,0,0,0,0]] * top_padding +
            [self.row.state] +
            [[0,0,0,0,0,0,0,0]] * bottom_padding
        ])

    def drop(self):
        previous_row = list()

        if self.board.towerHeight == 0:
            previous_row = [1,1,1,1,1,1,1,1]
        else:
            previous_row = self.board.fullState[-1]

        current_row = self.row.state.copy()

        after_row = list()

        for x in range(8):
            after_row.append(previous_row[x] and current_row[x])

        if after_row == [0,0,0,0,0,0,0,0]:
            self.lose()
            return

        self.board.add_row(after_row.copy())

        self.row.state = after_row

        self.draw(self.state)

    def lose(self):
        self.gameLoop.deinit()

        self.die_animation(self.state)

        self.board.fullState = []
        self.row.state = [0,0,0,0,1,1,1,1]
        self.row.direction = 'left' #one of 'left' or 'right'
        self.board.towerHeight = 0
        self.board.towerHeightOffset = 0

        self.gameLoop.init(mode=Timer.PERIODIC,
                           period=self.LOOP_SPEED,
                           callback=self.loop)

    def debug_print(self):
        print("\x1B\x5B2J", end="")
        print("\x1B\x5BH", end="")
        print(self.state)
        print(str(self.board.towerHeight) + ':' + str(self.board.towerHeightOffset))

    def loop(self,t):
        self.led.toggle()

        self.debug_print()

        self.row.move()

        self.draw(self.state)

    def run(self):
        print('starting stack')

        def up_fn(btn_pressed):    print('up')
        def down_fn(btn_pressed):  self.drop()
        def left_fn(btn_pressed):  print('left')
        def right_fn(btn_pressed): print('right')
        def a_fn(btn_pressed):     print('a')
        def b_fn(btn_pressed):     self.exit()

        self.controller.on_up(up_fn)
        self.controller.on_down(down_fn)
        self.controller.on_left(left_fn)
        self.controller.on_right(right_fn)
        self.controller.on_a(a_fn)
        self.controller.on_b(b_fn)

        self.display.fill(0)
        self.display.show()

        self.gameLoop.init(mode=Timer.PERIODIC,
                           period=self.LOOP_SPEED,
                           callback=self.loop)