from machine import Pin, SPI
import max7219
import time

class Display:

    def __init__(self):
        self.spi = SPI(0, baudrate=10000000, polarity=0, phase=0, sck=Pin(6), mosi=Pin(3))
        self.ss = Pin(5, Pin.OUT)
        display = max7219.Matrix8x8(self.spi, self.ss, 1)
        display.brightness(1)
        self.fill = display.fill
        self.pixel = display.pixel
        self.hline = display.hline
        self.vline = display.vline
        self.line = display.line
        self.text = display.text
        self.scroll = display.scroll
        self.show = display.show
        self.blit = display.blit
    # END OF __init__


    def splashscreen(self):
        self.showtext("G", 0, 1)
        time.sleep(0.8)
        self.showtext("B", 0, 1)
        time.sleep(0.8)
        self.showtext("P", 0, 1)
        time.sleep(0.8)
        self.fill(0)
        self.show()
        #self.reset()
        time.sleep(1)
    # END OF splashscreen()


    def clock(self):
        self.fill(0)
        self.pixel(3, 1, 1)
        self.pixel(4, 1, 1)
        self.pixel(2, 2, 1)
        self.pixel(5, 2, 1)
        self.pixel(1, 3, 1)
        self.pixel(6, 3, 1)
        self.pixel(1, 4, 1)
        self.pixel(6, 4, 1)
        self.pixel(2, 5, 1)
        self.pixel(5, 5, 1)
        self.pixel(3, 6, 1)
        self.pixel(4, 6, 1)
        self.pixel(3, 3, 1)
        self.show()
    # END OF clock()


    def showpixel(self, x, y):
        self.fill(0)
        self.pixel(x, y, 1)
        self.show()
    # END OF showpixel()


    def showtext(self, text, x, y):
        self.fill(0)
        self.text(text, x, y)
        self.show()
    # END OF showtext()


    def reset():
        self.fill(0)
        self.show()
    # END OF reset()