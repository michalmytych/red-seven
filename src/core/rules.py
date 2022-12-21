def highest_card_wins(players):  
  return max(players, key = lambda player: max(player.cards))
 

def most_of_one_number_wins(players):
  get_player_cards_numbers = lambda player: [card.number for card in player.cards]
  get_count_of_unique_cards = lambda player: len(set(get_player_cards_numbers(player)))
  return min(players, key = lambda player: get_count_of_unique_cards(player))


def most_of_one_color_wins(players):
  get_player_cards_colors = lambda player: [card.color for card in player.cards]
  get_count_of_unique_cards = lambda player: len(set(get_player_cards_colors(player)))
  return min(players, key = lambda player: get_count_of_unique_cards(player))


def most_even_cards_wins(players):
  get_player_even_cards = lambda player: [card for card in player.cards if card % 2 == 0]
  return max(players, lambda player: len(get_player_even_cards(player)))


def most_different_colors_wins(players):
  get_player_cards_colors = lambda player: [card.color for card in player.cards]
  get_count_of_unique_cards = lambda player: len(set(get_player_cards_colors(player)))
  return max(players, key = lambda player: get_count_of_unique_cards(player))


def most_cards_below_4_wins(players):
  get_player_cards_blow_4 = lambda player: [card.number for card in player.cards if card.number < 4]
  get_count_of_below_4_cards = lambda player: len(get_player_cards_blow_4(player))
  return min(players, key = lambda player: get_count_of_below_4_cards(player))

def most_cards_in_a_row_wins():
  pass
