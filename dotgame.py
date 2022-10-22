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