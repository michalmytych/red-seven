def highest_card_wins(players: list):  
  highest_cards = [player.highest_card() for player in players]
  draw = all(hc == highest_cards[0] for hc in highest_cards)
  if draw:
    return None
  return max(players, key = lambda player: player.highest_card())
 

def most_of_one_number_wins(players: list):
  """
    @todo
    na ten moment sprawdza po distinct ale powinno patrzeć zawsze na powtórzenia jednego numeru
    bo np (1,1,2,2,3) wygra nad (3,4,4,4,5) bo porówna len([1, 2]) z len([4]) a powinien wygrac
    ten drugi bo u niego powtarza sie 4 az 3 razy
  """
  get_player_cards_numbers = lambda player: [card.number for card in player.palette]
  get_count_of_unique_cards = lambda player: len(set(get_player_cards_numbers(player)))
  return min(players, key = lambda player: get_count_of_unique_cards(player))


def most_of_one_color_wins(players: list):
  get_player_cards_colors = lambda player: [card.color.strength for card in player.palette]
  get_count_of_unique_cards = lambda player: len(set(get_player_cards_colors(player)))
  return min(players, key = lambda player: get_count_of_unique_cards(player))


def most_even_cards_wins(players: list):
  get_player_even_cards = lambda player: [card for card in player.palette if card % 2 == 0]
  return max(players, key = lambda player: len(get_player_even_cards(player)))


def most_different_colors_win(players: list):
  get_player_cards_colors = lambda player: [card.color.strength for card in player.palette]
  get_count_of_unique_cards = lambda player: len(set(get_player_cards_colors(player)))
  return max(players, key = lambda player: get_count_of_unique_cards(player))


def most_cards_below_4_wins(players: list):
  get_player_cards_blow_4 = lambda player: [card.number for card in player.palette if card.number < 4]
  get_count_of_below_4_cards = lambda player: len(get_player_cards_blow_4(player))
  return min(players, key = lambda player: get_count_of_below_4_cards(player))

def most_cards_in_a_row_wins():
  return "NOT IMPLEMENTED"
