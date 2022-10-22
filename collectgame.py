# collect falling blocks
def collectgame():
  y = 7
  x = 3
  by = 0
  i = 0
  score = 0
  # x value of falling blocks
  b = [3, 4, 1, 2, 4, 5, 6, 1, 2, 7, 0, 3, 2]
  while True:
    display.fill(0)
    display.pixel(b[i], by, 1)
    display.pixel(x, y, 1)
    display.show()
    if controller.left() and x > 0:
      x = x - 1
    if controller.right() and x < 7:
      x = x + 1
    by = by + 1
    if(by == 9):
      by = 0
      i = i + 1
    if by == y and b[i] == x:
      score = score + 1
    time.sleep(0.2)
# END OF collectgame()
