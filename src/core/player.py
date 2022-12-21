from core.utils import random_pop
from core.card import Card

class Player:
  def __init__(self, id: int, cards: list):
    self.id = id
    # self.palette = [random_pop(cards)]  - poprawnie
    self.palette = cards # do testów
    self.hand = cards
    self.representation = f'Player id: {self.id}, palette: {self.palette}'

  def __str__(self):
    return self.representation

  def __repr__(self):
    return self.representation

  def play_to_palette(self, card: Card):
    pass

  def change_rule(self, card: Card):
    pass

  def play_to_palette_and_change_rule(self, to_palette: Card, to_rule: Card):
    pass
