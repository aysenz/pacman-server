from artifact_manager import ArtifactManager
from hero_manager import HeroManager
from physics import Physics

class Game():
  physics = Physics()
  def __init__(self):
    self.artifact_manager = ArtifactManager()
    self.hero_manager = HeroManager()
  def connect_new_gamer(self, id, name):
    self.hero_manager.add(id, name)
    return self.hero_manager.get(id)
  def disconnect_gamer(self, id):
    self.hero_manager.delete(id)
  def get_all_artifacts(self):
    all = []
    for a in self.artifact_manager.get_all():
      a = a.__dict__
      all.append(a)
    return all
  def get_all_heroes(self):
    all = []
    for a in self.hero_manager.get_all():
      a = a.__dict__
      all.append(a)
    return all
  def move(self, id, direction):
    self.hero_manager.move(id, direction)
    hero = self.hero_manager.get(id)
    r = { 'x': hero.x, 'y': hero.y, 'diameter': hero.diameter, 'eat': None }
    for artifact in self.artifact_manager.get_all():
      if self.physics.object_on_object(hero, artifact):
        self.hero_manager.eat_artifact(id, artifact)
        self.artifact_manager.delete(artifact.id)
        r['eat'] = artifact
    for another_hero in self.hero_manager.get_all():
      if self.physics.object_on_object(hero, another_hero) and another_hero.id != hero.id:
        self.hero_manager.eat_hero(id, another_hero)
        self.hero_manager.delete(another_hero.id)
        r['eat'] = another_hero
    return r