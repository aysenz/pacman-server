from random import random
import math
from enum import Enum

class ArtifactType():
  POTATO = 0
  POTION = 1
  MEATBALL = 2

class Artifact():
  COUNT_OF_TYPES = 3
  MIN_DIAMETER = 10
  def __init__(self, id, x, y, t=None):
    self.id = id
    self.x = x
    self.y = y
    self.diameter = self.MIN_DIAMETER
    self.type = math.floor(Artifact.COUNT_OF_TYPES * random())