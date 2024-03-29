#                             dP
#                             88
#  .d8888b. 88d888b. .d8888b. 88  .dP  .d8888b. .d8888b. .d8888b. 88d8b.d8b. .d8888b.    88d888b. dP    dP
#  Y8ooooo. 88'  `88 88'  `88 88888"   88ooood8 88'  `88 88'  `88 88'`88'`88 88ooood8    88'  `88 88    88
#        88 88    88 88.  .88 88  `8b. 88.  ... 88.  .88 88.  .88 88  88  88 88.  ... dP 88.  .88 88.  .88
#  `88888P' dP    dP `88888P8 dP   `YP `88888P' `8888P88 `88888P8 dP  dP  dP `88888P' 88 88Y888P' `8888P88
#                                                    .88                                 88            .88
#                                                d8888P                                  dP        d8888P

from machine import Timer
from game import Game
import time
import random

class FoodLayer:
    def __init__(self):
        self.state = [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
        ]

    def place_food(self, x, y):
        self.state[y][x] = 1

    def clear(self):
        self.state = [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
        ]

class SnakeLayer:
    def __init__(self, length, direction, startx, starty):
        self.length = length
        self.direction = direction  #one of 'up', 'down', 'left', 'right'
        self.headx = startx
        self.heady = starty
        self.collisionOccured = False
        self.state = [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
        ]
        self.state[self.heady][self.headx] = self.length

    def recalculate_state(self):
        # reduce all numbers on this layer by 1
        for y in range(8):
            for x in range(8):
                if self.state[y][x] > 0:
                    self.state[y][x] -= 1

        # place new head position
        self.state[self.heady][self.headx] = self.length

    def move_up(self):
        self.heady -= 1
        if self.heady < 0:
            self.heady = 7

    def move_down(self):
        self.heady += 1
        if self.heady > 7:
            self.heady = 0

    def move_left(self):
        self.headx -= 1
        if self.headx < 0:
            self.headx = 7

    def move_right(self):
        self.headx += 1
        if self.headx > 7:
            self.headx = 0

    def move(self, new_direction):
        # forbid moving the same direction you came from
        if (self.direction == 'up'    and new_direction == 'down' or
            self.direction == 'down'  and new_direction == 'up' or
            self.direction == 'left'  and new_direction == 'right' or
            self.direction == 'right' and new_direction == 'left'):
            new_direction = None

        if new_direction != None:
            self.direction = new_direction

        if self.direction == 'up':
            self.move_up()
        elif self.direction == 'down':
            self.move_down()
        elif self.direction == 'left':
            self.move_left()
        elif self.direction == 'right':
            self.move_right()

        # self collision check
        if self.state[self.heady][self.headx] > 0:
            self.collisionOccured = True

        self.recalculate_state()

    def lengthen(self):
        self.length += 1

class BoardLayer:
    def __init__(self):
        self.index = 0
        self.levels = [
            [
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0]
            ],
            [
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,1],
                [0,0,0,0,0,0,0,1],
                [0,0,0,0,0,0,0,1],
                [0,0,0,0,1,1,1,1]
            ],
            [
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,1,0,0,0,0],
                [0,0,0,1,0,0,0,0],
                [0,0,0,1,0,0,0,0],
                [0,0,0,1,0,0,0,0]
            ],
            [
                [1,1,1,1,1,1,1,1],
                [1,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0]
            ],
            [
                [1,1,1,1,1,1,1,1],
                [1,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,1],
                [1,1,1,1,1,1,1,1]
            ]
        ]

    def set_next_level(self):
        self.index += 1
        if self.index >= len(self.levels):
            self.index = 0

    def set_random_level(self):
        self.index = random.randint(0, len(self.levels) - 1)

    @property
    def state(self):
        return self.levels[self.index]

class SnakeGame(Game):
    def __init__(self, display, controller, menu):
        Game.__init__(self, display, controller, menu)
        self.snake = SnakeLayer(3, 'up', 6, 6) # SnakeLayer(length, direction, startx, starty)
        self.board = BoardLayer()
        self.food = FoodLayer()
        self.lastButtonPressed = None
        self.LOOP_SPEED = 250

    @property
    def state(self):
        return self.add_states([self.board.state, self.snake.state, self.food.state])

    def debug_print(self):
        print("\x1B\x5B2J", end="")
        print("\x1B\x5BH", end="")
        for y in range(8):
            for x in range(8):
                print(self.board.state[y][x] or self.snake.state[y][x] or self.food.state[y][x], end='')
            print('') # inserts a new line
        print('') # new line

    def lose(self):
        self.gameLoop.deinit()

        self.die_animation(self.state)
        self.score_animation(self.snake.length, self.state)

        # del self.snake
        # self.snake = self.snake = SnakeLayer(3, 'up', 6, 6)
        # self.gameLoop.init(mode=Timer.PERIODIC,
        #                    period=self.LOOP_SPEED,
        #                    callback=self.loop)

    def detect_collision(self):
        if (self.board.state[self.snake.heady][self.snake.headx] > 0): # collision with wall
            return True
        elif (self.snake.collisionOccured): # collision with self
            return True
        elif (self.food.state[self.snake.heady][self.snake.headx] > 0): # collision with food
            self.snake.lengthen()
            self.generate_food()

        return False

    def generate_food(self):
        self.food.clear()
        while True:
            x = random.randint(0,7)
            y = random.randint(0,7)
            if (not (self.board.state[y][x] or self.snake.state[y][x])):
                break
        self.food.place_food(x,y)

    def loop(self, t):
        self.led.toggle()

        self.snake.move(self.lastButtonPressed)
        self.draw(self.state)

        if(self.detect_collision()):
            self.lose()

        self.debug_print()

        self.lastButtonPressed = None

    def run(self):
        print('starting snake')

        def up_fn(btn_pressed): self.lastButtonPressed = 'up'
        def down_fn(btn_pressed): self.lastButtonPressed = 'down'
        def left_fn(btn_pressed): self.lastButtonPressed = 'left'
        def right_fn(btn_pressed): self.lastButtonPressed = 'right'
        def a_fn(btn_pressed): self.board.set_next_level()
        def b_fn(btn_pressed): self.exit()

        self.controller.on_up(up_fn)
        self.controller.on_down(down_fn)
        self.controller.on_left(left_fn)
        self.controller.on_right(right_fn)
        self.controller.on_a(a_fn)
        self.controller.on_b(b_fn)

        self.generate_food()

        self.draw(self.state)

        self.gameLoop.init(mode=Timer.PERIODIC,
                           period=self.LOOP_SPEED,
                           callback=self.loop)