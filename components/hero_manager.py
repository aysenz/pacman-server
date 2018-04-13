from hero import Hero

class HeroManager():
  def __init__(self):
    self._heroes = []
  def add(self, id, name):
    new_hero = Hero(id, name)
    self._heroes.append(new_hero)
  def get(self, id):
    index = self.get_index(id)
    return self._heroes[index]
  def get_index(self, id):
    for idx, h in enumerate(self._heroes):
      if h.id == id:
        return idx
    return None
  def get_all(self):
    return self._heroes
  def delete(self, id):
    index = self.get_index(id)
    del self._heroes[index]
  def move(self, id, direction):
    idx = self.get_index(id)
    if (type(idx) == None): return None
    self._heroes[idx].move(direction)
  def eat_artifact(self, id, artifact):
    idx = self.get_index(id)
    self._heroes[idx].eat_artifact(artifact)
  def eat_hero(self, id, another_hero):
    idx = self.get_index(id)
    if self._heroes[idx].eat_hero(another_hero):
      self.delete(another_hero.id)