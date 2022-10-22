import time
from button import Button
from machine import Timer, Pin
from display import Display
from controller import Controller

display = Display()


class Snake:
    
    def __init__(self, length, direction, startx, starty):
        self.length = length
        self.direction = direction  #one of 'up', 'down', 'left', 'right'
        self.headx = startx
        self.heady = starty

    def move(self, direction):
        if direction != None:
            #if ((self.direction == 'up'    and direction == 'down' ) or
            #    (self.direction == 'down'  and direction == 'up'   ) or
            #    (self.direction == 'left'  and direction == 'right') or
            #    (self.direction == 'right' and direction == 'left' )):
            self.direction = direction

        if self.direction == 'up':
            self.heady -= 1
        elif self.direction == 'down':
            self.heady += 1
        elif self.direction == 'left':
            self.headx -= 1
        elif self.direction == 'right':
            self.headx += 1

    def lengthen(self):
        self.length += 1

    def die(self):
        display.fill(1)
        display.show()


class Board:

    def __init__(self, snake):
        self.state = [
            ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
            ['w',  0 ,  0 ,  0 ,  0 ,  0 ,  0 , 'w'],
            ['w',  0 , 'a',  0 ,  0 ,  0 ,  0 , 'w'],
            ['w',  0 ,  0 ,  0 ,  0 ,  0 ,  0 , 'w'],
            ['w',  0 ,  0 ,  0 ,  0 ,  0 ,  0 , 'w'],
            ['w',  0 ,  0 ,  0 ,  0 ,  0 ,  0 , 'w'],
            ['w',  0 ,  0 ,  0 ,  0 ,  0 ,  0 , 'w'],
            ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
        ]
        self.snake = snake
        self.state[self.snake.headx][self.snake.heady] = self.snake.length

    def draw(self):
        for x in range(8):
            for y in range(8):
                if self.state[x][y] != 0:
                    display.pixel(x, y, 1)
                else:
                    display.pixel(x, y, 0)

        display.show()

    def detectCollision(self):
        if (self.state[self.snake.headx][self.snake.heady] != 0):
            return True
        else:
            return False
    
    def recalculateState(self):
        self.state[self.snake.headx][self.snake.heady] = self.snake.length
        for x in range(8):
            for y in range(8):
                currentpixel = self.state[x][y]
                if type(currentpixel) == int and currentpixel > 0:
                    self.state[x][y] -= 1

    def debugPrint(self):
        for y in range(8):
            for x in range(8):
                print(self.state[x][y], end='')
            print('')
        print('')


class SnakeGame:

    def __init__(self):
        self.controller = Controller()
        self.led = Pin(25, Pin.OUT)
        self.player = Snake(4, 'up', 6, 6)
        self.myBoard = Board(self.player)

    def loop(self, t):
        self.led.toggle()

        self.myBoard.recalculateState()
        if(self.myBoard.detectCollision()):
            self.player.die()
            t.deinit()

        #last press
        lp = self.controller.last_button_pressed

        self.player.move(lp)
        self.myBoard.draw()
        self.myBoard.debugPrint()
        
        self.controller.reset_press()

    def run(self):
        print('starting snake')
        self.myBoard.draw()

        game_loop_timer = Timer()
        game_loop_timer.init(mode=Timer.PERIODIC,
                             period=500,
                             callback=self.loop)

        # led_timer = Timer()
        # led_timer.init(mode=Timer.PERIODIC, period=250, callback=lambda t:led.toggle())


if __name__ == "__main__":
    game = SnakeGame()
    game.run()