from random import random
from map import Map
from artifact import Artifact, ArtifactType
from artifact_manager import ArtifactManager
from threading import Timer

class Hero():
  MIN_DIAMETER = 30
  MIN_SPEED = 3
  def __init__(self, id, name):
    self.id = id
    self.name = name
    self.x = Map.WIDTH * random()
    self.y = Map.HEIGHT * random()
    self.diameter = self.MIN_DIAMETER
    self.speed = self.MIN_SPEED
  def eat_artifact(self, artifact):
    if ArtifactType.POTATO == artifact.type:
      self.diameter += artifact.diameter
    elif ArtifactType.POTION == artifact.type:
      # self.diameter = self.MIN_DIAMETER
      if (self.diameter - artifact.diameter) >= self.MIN_DIAMETER:
        self.diameter = self.diameter - artifact.diameter
    elif ArtifactType.MEATBALL == artifact.type:
      self.speed += 1
      def fun():
        self.speed -= 1
      t = Timer(3.0, fun)
      t.start()
    ArtifactManager.eated_artifact(artifact)
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