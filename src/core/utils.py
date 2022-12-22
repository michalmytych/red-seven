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


def get_card_by_color_and_number(deck: list, number: int, color_name: str) -> Card:
  card_filter = lambda card: card.color.name == color_name and card.number == number
  found = list(filter(card_filter, deck))
  return found[0]
