import time
import machine
import random
from button import Button
from machine import Timer, Pin
from display import Display
from controller import Controller

class Food:
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

class Snake:
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
        for y in range(8):
            for x in range(8):
                if self.state[y][x] > 0:
                    self.state[y][x] -= 1
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
        #don't allow moving the same direction you came from
        if (self.direction == 'up' and new_direction == 'down' or
            self.direction == 'down' and new_direction == 'up' or
            self.direction == 'left' and new_direction == 'right' or
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

        if self.state[self.heady][self.headx] > 0:
            self.collisionOccured = True

        self.recalculate_state()

    def check_next(self):
        if self.direction == 'up':
            self.state. headx

    def lengthen(self):
        self.length += 1

class Board:
    def __init__(self, snake):
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

class SnakeGame:
    def __init__(self, display, controller, menu):
        self.menu = menu
        self.display = display
        self.controller = controller
        self.gameLoopTimer = Timer()
        self.led = Pin(25, Pin.OUT)
        self.snake = Snake(3, 'up', 6, 6)
        self.board = Board(self.snake)
        self.food = Food()
        self.lastButtonPressed = None

    def debug_print(self):
        print("\x1B\x5B2J", end="")
        print("\x1B\x5BH", end="")
        for y in range(8):
            for x in range(8):
                print(self.board.state[y][x] or self.snake.state[y][x] or self.food.state[y][x], end='')
            print('')
        print('')

    def draw(self):
        for y in range(8):
            for x in range(8):
                if self.board.state[y][x] or self.snake.state[y][x] or self.food.state[y][x] != 0:
                    self.display.pixel(x, y, 1)
                else:
                    self.display.pixel(x, y, 0)
        self.display.show()

    def lose(self):
        self.gameLoopTimer.deinit()
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
        self.gameLoopTimer.init(mode=Timer.PERIODIC,
                                period=250,
                                callback=self.loop)

    def exit(self):
        self.gameLoopTimer.deinit()
        self.menu.stop_running_game()

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
        self.draw()

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
        self.draw()

        self.gameLoopTimer.init(mode=Timer.PERIODIC,
                                period=250,
                                callback=self.loop)

        # led_timer = Timer()
        # led_timer.init(mode=Timer.PERIODIC, period=250, callback=lambda t:led.toggle())


if __name__ == "__main__":
    game = SnakeGame(Display(), Controller())
    game.run()


