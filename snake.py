import time
import machine
from button import Button
from machine import Timer, Pin
from display import Display
from controller import Controller

class Snake:

    def __init__(self, length, direction, startx, starty):
        self.length = length
        self.direction = direction  #one of 'up', 'down', 'left', 'right'
        self.headx = startx
        self.heady = starty

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
            #if ((self.direction == 'up'    and direction == 'down' ) or

            #    (self.direction == 'down'  and direction == 'up'   ) or
            #    (self.direction == 'left'  and direction == 'right') or
            #    (self.direction == 'right' and direction == 'left' )):
            self.direction = new_direction

        if self.direction == 'up':
            self.move_up()
        elif self.direction == 'down':
            self.move_down()
        elif self.direction == 'left':
            self.move_left()
        elif self.direction == 'right':
            self.move_right()

    def check_next(self):
        if self.direction == 'up':
            self.state. headx

    def lengthen(self):
        self.length += 1

class Board:

    def __init__(self, snake):
        # self.state = [
        #     [-1,-1,-1,-1,-1,-1,-1,-1],
        #     [-1, 0, 0, 0, 0, 0, 0,-1],
        #     [-1, 0, 0, 0, 0, 0, 0,-1],
        #     [-1, 0, 0, 0, 0, 0, 0,-1],
        #     [-1, 0, 0, 0, 0, 0, 0,-1],
        #     [-1, 0, 0, 0, 0, 0, 0,-1],
        #     [-1, 0, 0, 0, 0, 0, 0,-1],
        #     [-1,-1,-1,-1,-1,-1,-1,-1],
        # ]
        self.state = [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,-2,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
        ]
        self.snake = snake
        self.state[self.snake.headx][self.snake.heady] = self.snake.length

    def recalculateState(self):
        self.state[self.snake.headx][self.snake.heady] = self.snake.length
        for x in range(8):
            for y in range(8):
                currentpixel = self.state[x][y]
                if type(currentpixel) == int and currentpixel > 0:
                    self.state[x][y] -= 1

    def debugPrint(self):
        print("\x1B\x5B2J", end="")
        print("\x1B\x5BH", end="")
        for y in range(8):
            for x in range(8):
                print(self.state[x][y], end='')
            print('')
        print('')


class SnakeGame:

    def __init__(self, display, controller):
        self.display = display
        self.controller = controller
        self.game_loop_timer = Timer()
        self.led = Pin(25, Pin.OUT)
        self.player = Snake(6, 'up', 6, 6)
        self.myBoard = Board(self.player)
        self.last_button_pressed = None

    def detectCollision(self):
        if (self.myBoard.state[self.player.headx][self.player.heady] < self.player.length and self.myBoard.state[self.player.headx][self.player.heady] != 0):
            return True
        else:
            return False

    def draw(self, state):
        for x in range(8):
            for y in range(8):
                if state[x][y] != 0:
                    self.display.pixel(x, y, 1)
                else:
                    self.display.pixel(x, y, 0)
        self.display.show()

    def lose(self):
        self.display.fill(1)
        self.display.show()
        time.sleep_ms(100)
        self.draw(self.myBoard.state)
        time.sleep_ms(100)
        self.display.fill(1)
        self.display.show()
        time.sleep_ms(100)
        self.draw(self.myBoard.state)
        time.sleep_ms(100)
        self.display.fill(1)
        self.display.show()
        time.sleep_ms(100)

        self.game_loop_timer.deinit()
        machine.reset()

    def loop(self, t):
        self.led.toggle()

        if(self.detectCollision()):
            if self.myBoard.state[self.player.headx][self.player.heady] == -2:
                self.player.lengthen()
            else:
                self.lose()

        self.myBoard.recalculateState()

        self.player.move(self.last_button_pressed)
        self.draw(self.myBoard.state)
        self.myBoard.debugPrint()

        self.last_button_pressed = None

    def run(self):
        print('starting snake')

        def up_fn(btn_pressed): self.last_button_pressed = 'up'
        def down_fn(btn_pressed): self.last_button_pressed = 'down'
        def left_fn(btn_pressed): self.last_button_pressed = 'left'
        def right_fn(btn_pressed): self.last_button_pressed = 'right'
        def a_fn(btn_pressed): self.last_button_pressed = 'a'
        def b_fn(btn_pressed): machine.reset()

        self.controller.on_up(up_fn)
        self.controller.on_down(down_fn)
        self.controller.on_left(left_fn)
        self.controller.on_right(right_fn)
        self.controller.on_a(a_fn)
        self.controller.on_b(b_fn)

        self.draw(self.myBoard.state)


        self.game_loop_timer.init(mode=Timer.PERIODIC,
                             period=250,
                             callback=self.loop)

        # led_timer = Timer()
        # led_timer.init(mode=Timer.PERIODIC, period=250, callback=lambda t:led.toggle())


if __name__ == "__main__":
    game = SnakeGame(Display(), Controller())
    game.run()


