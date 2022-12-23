from random import randrange, shuffle
from core.config import COLORS
from core.color import Color
from core.card import Card


def random_pop(sequence):
  random_range = randrange(len(sequence))
  random_element = sequence.pop(random_range)
  return random_element


def generate_shuffled_deck() -> list:
  colors = [Color(*color) for color in COLORS]
  cards = [Card(number, color) for color in colors for number in range(1, 8)]
  shuffle(cards)
  return cards


def card(number: int, color_name: str):
  color_config = list(filter(lambda c: c[1] == color_name, COLORS))[0]
  color = Color(*color_config)
  card = Card(number, color)
  return card
