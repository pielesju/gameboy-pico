# ------------------------------------------------------------------------------
#  GameBoy Pico                                                                -
#  GNU GPL v3.0 License                                                        -
#                                                                              -
#  Julian Pieles                                                               -
#  Gabriel Walter                                                              -
#                                                                              -
#  Hausmesseprojekt E3FI2 2022                                                 -
#                                                                              -
#  17.09.2022                                                                  -
# ------------------------------------------------------------------------------
#                                                                              -
#    _____                      ____                                           -
#   / ____|                    |  _ \                                          -
#  | |  __  __ _ _ __ ___   ___| |_) | ___  _   _                              -
#  | | |_ |/ _` | '_ ` _ \ / _ \  _ < / _ \| | | |                             -
#  | |__| | (_| | | | | | |  __/ |_) | (_) | |_| |                             -
#   \_____|\__,_|_| |_| |_|\___|____/ \___/ \__, |                             -
#  |  __ (_)                                 __/ |                             -
#  | |__) |  ___ ___                        |___/                              -
#  |  ___/ |/ __/ _ \                                                          -
#  | |   | | (_| (_) |                                                         -
#  |_|   |_|\___\___/                                                          -
#                                                                              -
# ------------------------------------------------------------------------------


# GameBoy Pico Components
from display import Display
from controller import Controller

# Games
# from dotgame import DotGame - does not exist yet
#from tetrisblock import TetrisBlock

# Utils
import time

# ------------------------------------------------------------------------------
# - START                                                                      -
# ------------------------------------------------------------------------------

################################################################################

# Variables

# device drivers
display = Display()
controller = Controller()

# engine
# TODO create engine.py and Engine class for movement and animations in games

# menu data
menu_index = 0
game_selected = False
selected_game = 0
menu_entries = ["1", "2", "3", "4"]

# dotgame = DotGame(display, controller) - does not exist yet
# TODO game class and subclasses for every game


# Methods

# game selection menu
def menu():
    global display
    global menu_index
    global game_selected
    global selected_game
    global menu_entries

    while not game_selected:
        display.showtext(menu_entries[menu_index], 0, 1)
        if (controller.left()):
            menu_button_left()
        if (controller.right()):
            menu_button_right()
        if (controller.down()):
            game_selected = True

        time.sleep(0.1) # really necessary?
        # maybe the menu should only be updated when a button is pressed
        # so that the menu is less laggy

    return menu_index # selected_game
# END OF menu()


# game selection menu move left
def menu_button_left():
    global menu_entries
    global menu_index

    if (menu_index < 0):
        menu_index = len(menu_entries) - 1
    else:
        menu_index = menu_index - 1
# END OF menu_button_left()


# game sleection menu move right
def menu_button_right():
    global menu_entries
    global menu_index

    if (menu_index > len(menu_entries) - 1):
        menu_index = 0
    else:
        menu_index = menu_index + 1
# END OF menu_button_right()

# END OF game selection menu
################################################################################

# a "game" in which a point or pixel is moved with the 4 buttons
def dotgame():
    global display
    global controller
    x = 0
    y = 0

    while True:
        display.showpixel(x, y)
        if (controller.up()):
            y = y - 1
        if (controller.down()):
            y = y + 1
        if (controller.left()):
            x = x - 1
        if (controller.right()):
            x = x + 1

        # when the coordinates of the point overflow
        # they rollback to the "negative" value
        # exit right > enter left and visa versa
        if (x > 8):
            x = 0
        if (y > 8):
            y = 0
        if (x < -1):
            x = 7
        if (y < -1):
            y = 7

    #time.sleep(0.1)
# END OF dotgame()


def stackgame():
  global display
  global controller

  x = 1
  y = 6
  w = 6

  display.fill(0)
  display.hline(1, 7, 6, 1)
  display.show()
  pressed = False
  lines = [[1, 7, 6]]
  dir = "l"
  while True:
    for l in lines:
      display.hline(l[0],l[1],l[2],1)


    display.hline(x, y, w, 1)
    display.show()
    if(dir == "l"):
      x = x + 1
      if x > 8:
        dir = "r"

    if(dir == "r"):
      x = x - 1
      if x <= 0 - w:
        dir = "l"

    if(controller.down()):
      nx = x
      ny = y
      nw = w

      """
      oline = lines[len(lines) - 1]
      if oline[0] > nx:
        diff = oline[0] - nx
        nx = nx + diff
        wx = wx - diff
      """

      display.hline(nx, ny, nw, 1)
      if y < 3:
        for l in lines:
          l[1] = l[1] + 1
        y = y + 1

      display.show()
      lines.append([x, y, w])
      x = 1
      y = y - 1
      pressed = True

    time.sleep(0.1)
    display.fill(0)
# END OF stackgame()


def tetris():
    y = 0
    x = 0
    blocks = []
    while True:
        display.fill(0)
        display.pixel(0 + x,0 + y,1)
        display.pixel(1 + x,0 + y,1)
        display.pixel(2 + x,0 + y,1)
        display.pixel(2 + x,1 + y,1)

        display.show()
        time.sleep(0.3)
        if controller.left() and y + 3 < 7:
            x = x - 1
        if controller.right() and y + 3 < 7:
            x = x + 1
        if(y + 3 < 7):
            y = y + 1
# END OF tetris()


# collect falling blocks
def collectgame():
  y = 7
  x = 3
  by = 0
  i = 0
  score = 0
  # x value of falling blocks
  b = [3, 4, 1, 2, 4, 5, 6, 1, 2, 7, 0, 3, 2]
  while True:
    display.fill(0)
    display.pixel(b[i], by, 1)
    display.pixel(x, y, 1)
    display.show()
    if controller.left() and x > 0:
      x = x - 1
    if controller.right() and x < 7:
      x = x + 1
    by = by + 1
    if(by == 9):
      by = 0
      i = i + 1
    if by == y and b[i] == x:
      score = score + 1
    time.sleep(0.2)
# END OF collectgame()


# Main Method
# runs until the device is killed by physically shut off
# the print output
def run():
    print("Hello World")
    display.splashscreen()
    print("boot finished")

    while True:
        print("menu")
        selected_game = menu()
        print("selected game: " + selected_game)

        if (selected_game == 0):
            print("dotgame")
            dotgame()
        elif (selected_game == 1):
            print("stackgame")
            stackgame()
        elif (selected_game == 2):
            print("tetris")
            tetris()
        elif (selected_game == 3):
            print("collectgame")
            collectgame()
        else:
            break # restart console when no game is defined for selected_game
# END OF run()


#  finally running the program
# this should be the only method running in the class
run()

################################################################################

# ------------------------------------------------------------------------------
# - END                                                                        -
# ------------------------------------------------------------------------------
