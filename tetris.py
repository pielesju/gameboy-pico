
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