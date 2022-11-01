class Board:
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

    def draw(self):
        for x in range(8):
            for y in range(8):
                if self.state[x][y] != 0:
                    display.pixel(x, y, 1)
                else:
                    display.pixel(x, y, 0)
        display.show()

class block:
    def __init__(self):
        self.state = [0,0,0,0,1,1,1,1]
        self.direction = 'left' #one of 'left' or 'right'

    def move_left(self):
        for x in range(8):
            if self.state[x] == 1:
                self.state[x-1] = 1
                
    def move_right(self):
        for x in range(8):
            if self.state[x] == 1:
                self.state[x+1] = 1

class StackGame:
    def __init__(self, display, controller):
        self.display = display
        self.controller = controller
        self.led = Pin(25, Pin.OUT)

    def loop(self,t):
        self.led.toggle()


    def run(self):
        game_loop_timer = Timer()
        game_loop_timer.init(mode=Timer.PERIODIC,
                             period=1000,
                             callback=self.loop)
if __name__ == "__main__":
    game = StackGame(Display(), Controller())
    game.run()


