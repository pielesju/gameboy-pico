from machine import Pin
# Import MicroPython libraries of PIN and SPI
from machine import Pin, SPI

# Import MicoPython max7219 library
import max7219

from controller import Controller

# Import time
import time

# Intialize the SPI
spi = SPI(0, baudrate=10000000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3))
ss = Pin(5, Pin.OUT)

# Create matrix display instant, which has four MAX7219 devices.
display = max7219.Matrix8x8(spi, ss, 1)

controller = Controller()

# Set the display brightness. Value is 1 to 15.
display.brightness(10)

# Define the scrolling message
scrolling_message = "RASPBERRY PI PICO AND MAX7219 -- 8x8 DOT MATRIX SCROLLING DISPLAY"

# Get the message length
length = len(scrolling_message)

# Calculate number of columns of the message
column = (length * 8)

# Clear the display.
display.fill(0)
display.show()

# sleep for one one seconds
time.sleep(1)

x = 0
y = 0
w = 8

# Unconditionally execute the loop
while True:
    display.fill(0)
    display.pixel(x, y, 1)
    display.show()
    if (controller.up()):
        y = y - 1
    if (controller.down()):
        y = y + 1
    if (controller.left()):
        x = x + 1
    if (controller.right()):
        x = x - 1

    if (x > 8):
        x = 0
    if (y > 8):
        y = 0
    if (x < -1):
        x = 7
    if (y < -1):
        y = 7

    time.sleep(0.1)
    '''
    display.hline(x, y, w, 1)
    display.vline(x, y, w, 1)
    display.show()
    time.sleep(0.2)
    y = y + 1
    x = x + 1
    if(y > 7):
      y = -1
    if(x > 7):
      x = -1
    '''
