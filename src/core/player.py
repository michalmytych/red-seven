from core.utils import random_pop
from core.card import Card


class Player:
  def __init__(self, id: int, cards: list = [], palette: list = []):
    self.id = id
    self.palette = palette if len(palette) != 0 else [random_pop(cards)]
    self.hand = cards
    self.representation = f'(Player id: {self.id}, palette: {self.palette})'

  def __str__(self):
    return self.representation

  def __repr__(self):
    return self.representation

  def play_to_palette(self, card: Card):
    pass

  def change_rule(self, card: Card):
    pass

  def highest_card(self):
    return max(self.palette)

  def play_to_palette_and_change_rule(self, to_palette: Card, to_rule: Card):
    pass
