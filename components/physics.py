import math

class Physics():
  def object_on_object(self, object_a, object_b):
    diff = self._get_diff(object_a, object_b)
    distance = self._get_distance(diff)
    critical_distance = self._get_critical_distance(object_a, object_b)
    return True if distance < critical_distance else False
  def _get_diff(self, object_a, object_b):
    diff_by_x = 0; diff_by_y = 0
    if object_a.x > object_b.x: diff_by_x = object_a.x - object_b.x
    if object_a.x < object_b.x: diff_by_x = object_b.x - object_a.x
    if object_a.y > object_b.y: diff_by_y = object_a.y - object_b.y
    if object_a.y < object_b.y: diff_by_y = object_b.y - object_a.y
    return { 'x': diff_by_x, 'y': diff_by_y } 
  def _get_distance(self, diff):
    # pifagor)
    a = math.pow(diff['x'], 2)
    b = math.pow(diff['y'], 2)
    c = a + b
    return math.sqrt(c)
  def _get_critical_distance(self, object_a, object_b):
    return (object_a.diameter + object_b.diameter) / 2