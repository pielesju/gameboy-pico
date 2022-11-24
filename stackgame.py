from display import Display
from controller import Controller
from machine import Timer, Pin
from game import Game
import machine
import time

class Board:
    def __init__(self):
        self.state = []

    def add_row(self, row):
        self.state.append(row)

    def debugPrint(self):
        print("\x1B\x5B2J", end="")
        print("\x1B\x5BH", end="")
        print(self.state)
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
        self.length = 4

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
        self.board = Board()
        self.row = Row()
        self.towerHeight = 0
        self.towerHeightOffset = 0

    def draw(self):
        state = (self.board.state + [self.row.state])[self.towerHeightOffset:self.towerHeight+1]
        for y in range(8):
            for x in range(8):
                try:
                    self.display.pixel(x, -y+7, state[y][x]) # withuot -y+7 the game will be upside down
                except IndexError:
                    self.display.pixel(x, -y+7, 0)
        self.display.show()

    def drop(self):

        previous_row = list()

        if self.towerHeight == 0:
            previous_row = [1,1,1,1,1,1,1,1]
        else:
            previous_row = self.board.state[self.towerHeight-1]

        current_row = self.row.state.copy()

        after_row = list()

        for x in range(8):
            after_row.append(previous_row[x] and current_row[x])

        if after_row == [0,0,0,0,0,0,0,0]:
            self.lose()
            return

        self.board.add_row(after_row.copy())

        self.row.state = after_row

        self.towerHeight += 1
        if self.towerHeight >= 7:
            self.towerHeightOffset += 1


        self.draw()

    def lose(self):
        self.gameLoop.deinit()
        self.display.fill(1)
        self.display.show()
        time.sleep_ms(100)
        self.draw()
        time.sleep_ms(100)
        self.display.fill(1)
        self.display.show()
        time.sleep_ms(100)
        self.draw()
        time.sleep_ms(100)
        self.display.fill(1)
        self.display.show()
        time.sleep_ms(100)
        self.draw()

        del self.snake
        self.snake = self.snake = Snake(3, 'up', 6, 6)
        self.gameLoop.init(mode=Timer.PERIODIC,
                                period=250,
                                callback=self.loop)


    def loop(self,t):
        self.led.toggle()
        print("\x1B\x5B2J", end="")
        print("\x1B\x5BH", end="")
        print(self.board.state + [self.row.state])
        print(str(self.towerHeightOffset) + ':' + str(self.towerHeight))

        self.row.move()

        self.draw()



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
                                period=200,
                                callback=self.loop)
if __name__ == "__main__":
    game = StackGame(Display(), Controller())
    game.run()