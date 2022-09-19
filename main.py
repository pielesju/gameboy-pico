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


# Variables
display = Display()
controller = Controller()
menu_index = 0
game_selected = False
selected_game = 0
menu_entries = ["1", "2", "3"]
# dotgame = DotGame(display, controller) - does not exist yet


# Methods

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

    time.sleep(0.1)
  
  return menu_index
# END OF menu()


def menu_button_left():
  global menu_entries
  global menu_index

  if (menu_index < 0):
    menu_index = len(menu_entries) - 1
  else:
    menu_index = menu_index - 1
# END OF menu_button_left()


def menu_button_right():
  global menu_entries
  global menu_index

  if (menu_index > len(menu_entries) - 1):
    menu_index = 0
  else:
    menu_index = menu_index + 1
# END OF menu_button_right()


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
      lines.append([x, y ,w])
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

# Main Method
# runs until the device is killed by physically shut off
def run():
  display.splashscreen()
  
  while True:
    selected_game = menu()

    if (selected_game == 0):
      dotgame()
    elif (selected_game == 1):
      stackgame()
    elif (selected_game == 2):
      tetris()
# END OF run()


#  finally running the program
run()


# ------------------------------------------------------------------------------
# - END                                                                        -
# ------------------------------------------------------------------------------