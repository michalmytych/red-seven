import unittest
import core.rules as rules
from core.player import Player
from core.utils import generate_shuffled_deck, get_card_by_color_and_number

"""
@todo
testy dla wszystkich rules
"""
class TestRules(unittest.TestCase):
  def __init__(self, *args, **kwargs):
    self.deck = generate_shuffled_deck()
    super(TestRules, self).__init__(*args, **kwargs)

  def test_highest_card_wins_by_number(self):
    players = [
      Player(0, [
        get_card_by_color_and_number(self.deck, 6, "red")
      ]),
      Player(1, [
        get_card_by_color_and_number(self.deck, 7, "red")
      ]),
    ]
    winner = rules.highest_card_wins(players)
    self.assertEqual(winner.id, 1)

  def test_highest_card_wins_by_color(self):
    players = [
      Player(1, [
        get_card_by_color_and_number(self.deck, 7, "blue")
      ]),
      Player(2, [
        get_card_by_color_and_number(self.deck, 7, "red")
      ]),
    ]
    winner = rules.highest_card_wins(players)
    self.assertEqual(winner.id, 2)

  def test_highest_card_wins_draw(self):
    players = [
      Player(1, [
        get_card_by_color_and_number(self.deck, 7, "red")
      ]),
      Player(2, [
        get_card_by_color_and_number(self.deck, 7, "red")
      ]),
    ]
    winner = rules.highest_card_wins(players)
    self.assertEqual(winner, None)


if __name__ == '__main__':
  unittest.main()
