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
from menu import Menu

# Games
# from dotgame import DotGame - does not exist yet
#from tetrisblock import TetrisBlock
from asyncdebug import AsyncDebug
from snake import SnakeGame

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


# dotgame = DotGame(display, controller) - does not exist yet
# TODO game class and subclasses for every game


# Methods



# END OF game selection menu
################################################################################

# Main Method
# runs until the device is killed by physically shut off
# the print output
def run():

    games = [
        AsyncDebug(display, controller),
        SnakeGame(display, controller)
    ]

    # display.splashscreen()
    # game = AsyncDebug(display, controller)
    # game.run()
    menu = Menu(display, controller, games)
    menu.run()

    # while True:
    #     selected_game = menu()

    #     if (selected_game == 0):
    #         print("dotgame")
    #         dotgame()
    #     elif (selected_game == 1):
    #         print("stackgame")
    #         stackgame()
    #     elif (selected_game == 2):
    #         print("tetris")
    #         tetris()
    #     elif (selected_game == 3):
    #         print("collectgame")
    #         collectgame()
    #     else:
    #         break # restart console when no game is defined for selected_game
# END OF run()


#  finally running the program
# this should be the only method running in the class
run()

################################################################################

# ------------------------------------------------------------------------------
# - END                                                                        -
# ------------------------------------------------------------------------------
