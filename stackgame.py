
def stackgame():
  global display
  global controller

  x = 1
  y = 6
  w = 6

  display.fill(0)
  display.hline(1, 7, 6, 1)
  display.show()
  pressed = False
  lines = [[1, 7, 6]]
  dir = "l"
  while True:
    for l in lines:
      display.hline(l[0],l[1],l[2],1)


    display.hline(x, y, w, 1)
    display.show()
    if(dir == "l"):
      x = x + 1
      if x > 8:
        dir = "r"

    if(dir == "r"):
      x = x - 1
      if x <= 0 - w:
        dir = "l"

    if(controller.down()):
      nx = x
      ny = y
      nw = w

      """
      oline = lines[len(lines) - 1]
      if oline[0] > nx:
        diff = oline[0] - nx
        nx = nx + diff
        wx = wx - diff
      """

      display.hline(nx, ny, nw, 1)
      if y < 3:
        for l in lines:
          l[1] = l[1] + 1
        y = y + 1

      display.show()
      lines.append([x, y, w])
      x = 1
      y = y - 1
      pressed = True

    time.sleep(0.1)
    display.fill(0)
# END OF stackgame()