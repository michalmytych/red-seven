from core.helpers import random_pop

class Player:
  def __init__(self, id, cards):
    self.id = id
    self.palette = [random_pop(cards)]
    self.hand = cards

  def play_to_palette(self, card):
    pass

  def change_rule(self, card):
    pass

  def play_to_palette_and_change_rule(self, to_palette, to_rule):
    pass
