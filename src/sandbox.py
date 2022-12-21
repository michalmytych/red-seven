from core.utils import generate_shuffled_deck, random_pop
from core.player import Player
import core.rules as rules

"""
@todo
Remove sandbox
"""

deck = generate_shuffled_deck()

def deal_seven_covered_cards():
  return [random_pop(deck) for n in range(0, 7)]

players = [
  Player(0, deal_seven_covered_cards()),
  Player(1, deal_seven_covered_cards())
]

for p in players:
  print(p)

print('*******************************START***GAME*******************************')

print('highest_card_wins')
print(rules.highest_card_wins(players))
print('\n\n')
print('most_of_one_number_wins')
print(rules.most_of_one_number_wins(players))
print('\n\n')
print('most_of_one_color_wins')
print(rules.most_of_one_color_wins(players))
print('\n\n')
print('most_even_cards_wins')
print(rules.most_even_cards_wins(players))
print('\n\n')
print('most_different_colors_win')
print(rules.most_cards_in_a_row_wins(players))
