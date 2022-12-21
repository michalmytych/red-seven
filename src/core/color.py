class Color:
  def __init__(self, strength: int, name: str, rule):
    self.strength = strength
    self.name = name
    self.rule = rule

  def __repr__(self):
    return self.name

  def __str__(self):
    return self.name

  def __eq__(self, color: object):
    return self.strength == color.strength

  def __lt__(self, color: object):
    return self.strength < color.strength

  def __gt__(self, color: object):
    return self.strength > color.strength

