from display import Display
from controller import Controller
from machine import Timer, Pin

class Board:
    def __init__(self):
        self.state = list()

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
        if self.direction == 'left' and self.state[0] == 1:
            self.direction = 'right'

        elif self.direction == 'right' and self.state[7] == 1:
            self.direction = 'left'

        if self.direction == 'left':
            self.move_left()
        elif self.direction == 'right':
            self.move_right()
        else:
            raise Exception("couldn't decide to move left or right")

class StackGame:
    def __init__(self, display, controller):
        self.display = display
        self.controller = controller
        self.led = Pin(25, Pin.OUT)
        self.board = Board()
        self.row = Row()
        self.tower_height = 0
        self.tower_height_offset = 0

    def draw(self, state):
        for x in range(8):
            for y in range(8):
                if state[x][y] != 0:
                    self.display.pixel(x, y, 1)
                else:
                    self.display.pixel(x, y, 0)
        self.display.show()

    def drop(self):

        self.board.state.push(self.row.state)

        # previous_state = list()

        # if self.tower_height == 0:
        #     previous_state = [1,1,1,1,1,1,1,1]
        # else:
        #     previous_state = self.board.state[self.tower_height-1]
        
        # dropped_state = self.row.state.copy()

        # after_state = list()

        # for x in range(8):
        #     after_state.append(previous_state[x] and dropped_state[x])

        # print(previous_state)
        # print(dropped_state)
        # print(after_state)

        # self.row.state = after_state
        # self.board.state[self.tower_height] = after_state.copy()
        # self.tower_height += 1
        # if self.tower_height >= 6:
        #     self.tower_height_offset += 1

    def loop(self,t):
        self.led.toggle()

        self.row.move()

        self.board.state[self.tower_height-self.tower_height_offset] = self.row.state
        self.draw(self.board.state)

    def run(self):
        print('starting stack')
 

        def up_fn(btn_pressed): print('up')
        def down_fn(btn_pressed): self.drop()
        def left_fn(btn_pressed): print('left')
        def right_fn(btn_pressed): print('right')
        def a_fn(btn_pressed): print('a')
        def b_fn(btn_pressed): print('b')

        self.controller.on_up(up_fn)
        self.controller.on_down(down_fn)
        self.controller.on_left(left_fn)
        self.controller.on_right(right_fn)
        self.controller.on_a(a_fn)
        self.controller.on_b(b_fn)

        self.display.fill(0)
        self.display.show()

        game_loop_timer = Timer()
        game_loop_timer.init(mode=Timer.PERIODIC,
                             period=200,
                             callback=self.loop)
if __name__ == "__main__":
    game = StackGame(Display(), Controller())
    game.run()


