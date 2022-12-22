import unittest
import core.rules as rules
from core.player import Player
import core.utils as utils


class TestRules(unittest.TestCase):
  def __init__(self, *args, **kwargs):
    self.deck = utils.generate_shuffled_deck()
    super(TestRules, self).__init__(*args, **kwargs)

  def test_highest_card_wins_by_number(self):
    players = [
      Player(0, [
        utils.get_card_by_color_and_number(self.deck, 6, "red")
      ]),
      Player(1, [
        utils.get_card_by_color_and_number(self.deck, 7, "red")
      ]),
    ]
    winner = rules.highest_card_wins(players)
    self.assertEqual(winner.id, 1)

  def test_highest_card_wins_by_color(self):
    players = [
      Player(1, [
        utils.get_card_by_color_and_number(self.deck, 7, "blue")
      ]),
      Player(2, [
        utils.get_card_by_color_and_number(self.deck, 7, "red")
      ]),
    ]
    winner = rules.highest_card_wins(players)
    self.assertEqual(winner.id, 2)

  def test_highest_card_wins_draw(self):
    players = [
      Player(1, [
        utils.get_card_by_color_and_number(self.deck, 7, "red")
      ]),
      Player(2, [
        utils.get_card_by_color_and_number(self.deck, 7, "red")
      ]),
    ]
    winner = rules.highest_card_wins(players)
    self.assertEqual(winner, None)

  def test_most_of_one_number_wins_simple(self):
    players = [
      Player(1, [
        utils.get_card_by_color_and_number(self.deck, 1, "red"),
        utils.get_card_by_color_and_number(self.deck, 7, "red")
      ]),
      Player(2, [
        utils.get_card_by_color_and_number(self.deck, 7, "red"),
        utils.get_card_by_color_and_number(self.deck, 7, "red")
      ]),
    ]
    winner = rules.most_of_one_number_wins(players)
    self.assertEqual(winner.id, 2)

  def test_most_of_one_number_wins_different_colors(self):
    players = [
      Player(1, [
        utils.get_card_by_color_and_number(self.deck, 7, "blue"),
        utils.get_card_by_color_and_number(self.deck, 2, "red")
      ]),
      Player(2, [
        utils.get_card_by_color_and_number(self.deck, 7, "indigo"),
        utils.get_card_by_color_and_number(self.deck, 7, "yellow")
      ]),
    ]
    winner = rules.most_of_one_number_wins(players)
    self.assertEqual(winner.id, 2)

  def test_most_of_one_number_wins_complicated(self):
    players = [
      Player(1, [
        utils.get_card_by_color_and_number(self.deck, 7, "blue"),
        utils.get_card_by_color_and_number(self.deck, 7, "red"),
        utils.get_card_by_color_and_number(self.deck, 2, "yellow"),
        utils.get_card_by_color_and_number(self.deck, 2, "indigo"),        
      ]),
      Player(2, [
        utils.get_card_by_color_and_number(self.deck, 3, "indigo"),
        utils.get_card_by_color_and_number(self.deck, 3, "yellow"),
        utils.get_card_by_color_and_number(self.deck, 3, "blue"),
      ]),
    ]
    winner = rules.most_of_one_number_wins(players)
    self.assertEqual(winner.id, 2)

if __name__ == '__main__':
  unittest.main()
