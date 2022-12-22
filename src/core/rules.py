import core.helpers as helpers

def highest_card_wins(players: list):  
  highest_cards = [player.highest_card() for player in players]
  draw = helpers.all_in_list_same(highest_cards)
  if draw:
    return None
  return max(players, key = lambda player: player.highest_card())
 

def most_of_one_number_wins(players: list):
  players_cards_numbers = []
  for player in players:
    cards = [card.number for card in player.palette]
    player_with_cards = {"cards": cards, "player_id": player.id}
    players_cards_numbers.append(player_with_cards)
  counts = []
  for player_with_cards in players_cards_numbers:
    counts_dict = dict()
    counts_dict["counts"] = helpers.get_items_count_dict(player_with_cards["cards"])
    counts_dict["player_id"] = player_with_cards["player_id"]
    counts.append(counts_dict)
  max_counts = list(map(lambda pc: max(list(pc["counts"].values())), counts))
  if helpers.all_in_list_same(max_counts):
    return None
  max_count = max(counts, key = lambda pc: max(list(pc["counts"].values())))
  winners = list(filter(lambda p: p.id == max_count["player_id"], players))
  return winners[0]


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
