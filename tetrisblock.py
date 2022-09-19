class TetrisBlock:
  def __init__(self, type)
    self. type = type
    self.fig = []

  def createfigure(self):
    if(self.type = 0):
      return [[0,0][0,1][1,0][1,1]]
    if(self.type = 1):
      return [[0,0][0,1][0,2][0,3]]

  def rotate(self):
    for t in self.fig:
      x = t[0]
      t[0] = t[1]
      t[1] = x