from random import random
from map import Map
from artifact import Artifact
from threading import Timer

class Hero():
  MIN_DIAMETER = 30
  MIN_SPEED = 3
  def __init__(self, id, name):
    self.id = id
    self.name = name
    map = Map()
    self.x = map.get_size('x') * random()
    self.y = map.get_size('y') * random()
    self.diameter = self.MIN_DIAMETER
    self.speed = self.MIN_SPEED
  def eat_artifact(self, artifact):
    diameter_diff = artifact.diameter / self.diameter
    if Artifact.TYPES['POTATO'] == artifact.type:
      self.diameter += diameter_diff * self.MIN_DIAMETER 
    elif Artifact.TYPES['POTION'] == artifact.type:
      if self.diameter >= self.MIN_DIAMETER:
        self.diameter -= diameter_diff * self.MIN_DIAMETER
        if self.diameter < self.MIN_DIAMETER: self.diameter = self.MIN_DIAMETER
    elif Artifact.TYPES['MEATBALL'] == artifact.type:
      self.speed += 2
      def fun():
        self.speed -= 2
      t = Timer(3.0, fun)
      t.start()
  def eat_hero(self, hero):
    return
  def die(self):
    return
  def move(self, direction):
    if direction == 'left':
      self.x -= self.speed
    elif direction == 'right':
      self.x += self.speed
    elif direction == 'up':
      self.y -= self.speed
    elif direction == 'down':
      self.y += self.speed