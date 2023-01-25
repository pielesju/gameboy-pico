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
#   .88888.                                888888ba                            -
#  d8'   `88                               88    `8b                           -
#  88        .d8888b. 88d8b.d8b. .d8888b. a88aaaa8P' .d8888b. dP    dP         -
#  88   YP88 88'  `88 88'`88'`88 88ooood8  88   `8b. 88'  `88 88    88         -
#  Y8.   .88 88.  .88 88  88  88 88.  ...  88    .88 88.  .88 88.  .88         -
#   `88888'  `88888P8 dP  dP  dP `88888P'  88888888P `88888P' `8888P88         -
#                                                                  .88         -
#                                                              d8888P          -
#   888888ba  oo                                                               -
#   88    `8b                                                                  -
#  a88aaaa8P' dP .d8888b. .d8888b.                                             -
#   88        88 88'  `"" 88'  `88                                             -
#   88        88 88.  ... 88.  .88                                             -
#   dP        dP `88888P' `88888P'                                             -
#                                                                              -
# ------------------------------------------------------------------------------

# GameBoy Pico Components
from display import Display
from controller import Controller
from menu import Menu

display = Display()
controller = Controller()

def run():

    display.splashscreen()
    menu = Menu(display, controller)
    menu.run()

run()