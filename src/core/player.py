from core.utils import random_pop
from core.card import Card
from core.palette import Palette

class Player:
  def __init__(self, id: int, hand: list = [], palette: Palette = None):
    self.id = id
    if not palette or len(palette.cards) == 0:
      palette = Palette([random_pop(hand)])
    self.palette = palette
    self.hand = hand
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
    return max(self.palette.cards)

  def play_to_palette_and_change_rule(self, to_palette: Card, to_rule: Card):
    pass
