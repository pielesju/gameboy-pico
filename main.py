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
from asyncdebug import AsyncDebug

# Utils
import time
from machine import Timer

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

# Main Method
# runs until the device is killed by physically shut off
# the print output
def run():
    display.splashscreen()

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
