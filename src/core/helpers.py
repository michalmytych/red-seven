from random import randrange, shuffle
from config import COLORS
from color import Color


def random_pop(sequence):
  random_range = randrange(len(sequence))
  random_element = sequence.pop(random_range)
  return random_element


def generate_shuffled_deck():
  cards = [Color(color[0], color[1]) for color in COLORS]
  shuffle(cards)
  return cards
