from artifact import Artifact
import math
from random import random
from map import Map

class ArtifactManager():
  _artifacts = []
  _counter_of_id = 0
  def __init__(self, min=100, max=150):
    self._min = min
    self._max = max
    self.create_all()
  def get_all(self):
    return self._artifacts
  def create(self, type=None):
    map = Map()
    x = map.get_size('x') * random()
    y = map.get_size('y') * random()
    self._counter_of_id += 1
    artifact = Artifact(self._counter_of_id, x, y, type)
    self._artifacts.append(artifact)
  def create_all(self):
    i = 0; rand_count = self._min + ((self._max - self._min) * random())
    while i < rand_count:
      self.create(None)
      i += 1
  def delete(self, id):
    idx = self.get_index(id)
    del self._artifacts[idx]
  def get_index(self, id):
    for idx, a in enumerate(self._artifacts):
      if a.id == id:
        return idx
    return None