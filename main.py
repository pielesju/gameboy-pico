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

# Utils
import time
from machine import Timer

# ------------------------------------------------------------------------------
# - START                                                                      -
# ------------------------------------------------------------------------------

################################################################################

# device drivers
display = Display()
controller = Controller()

################################################################################

# Main Method
# runs until the device is killed by physically shut off
# the print output
def run():

    display.splashscreen()
    menu = Menu(display, controller)
    menu.run()

#  finally running the program
# this should be the only method running in the class
run()

################################################################################

# ------------------------------------------------------------------------------
# - END                                                                        -
# ------------------------------------------------------------------------------
