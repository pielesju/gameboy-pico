from machine import Pin
import time

class Button:

  def __init__(self, pin):
    self.pin = pin
    self.btn = Pin(self.pin, Pin.IN, Pin.PULL_DOWN)

  def is_pressed(self):
    time.sleep_ms(50)
    if not self.btn.value():
      return False
    elif self.btn.value():
      return True