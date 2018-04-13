class Map():
  WIDTH = 1920
  HEIGHT = 1680
  def __init__(self):
    return
  def get_size(self, t=None):
    if (type(t) != None):
      if t == 'x': return self.WIDTH
      elif t == 'y': return self.HEIGHT
    return { 'width': self.WIDTH, 'height': self.HEIGHT }