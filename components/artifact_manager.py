from artifact import Artifact, ArtifactType
import math
from random import random
from map import Map
import thread
import time

class ArtifactManager():
  _artifacts = []
  _eated_artifacts = []
  _counter_of_id = 0
  _th_has_been_started = False
  def __init__(self, min=100, max=150):
    self._min = min
    self._max = max
    self.create_all()
  def balance(self):
    new_artifacts = []
    for a in ArtifactManager._eated_artifacts:
      if a.type == ArtifactType.POTATO:
        new_artifact = self.create(ArtifactType.POTION)
      elif a.type == ArtifactType.POTION:
        new_artifact = self.create(ArtifactType.POTATO)
      elif a.type == ArtifactType.MEATBALL:
        new_artifact = self.create(ArtifactType.MEATBALL)
      new_artifacts.append(new_artifact.__dict__)
      ArtifactManager._eated_artifacts.remove(a)
    return new_artifacts
  @staticmethod
  def eated_artifact(artifact):
    ArtifactManager._eated_artifacts.append(artifact)
  def get_all(self):
    return self._artifacts
  def create(self, type=None):
    x = Map.WIDTH * random()
    y = Map.HEIGHT * random()
    self._counter_of_id += 1
    artifact = Artifact(self._counter_of_id, x, y, type)
    self._artifacts.append(artifact)
    return artifact
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