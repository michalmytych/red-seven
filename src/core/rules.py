import core.helpers as helpers


def max_score_rule(players: list, method):
  players_scores = [
    {"player": player, "score": method(player)} 
    for player in players
  ]
  unique_scores_count = set([ps["score"] for ps in players_scores])
  if len(unique_scores_count) == 1:
    return None
  max_score = max(players_scores, key=lambda ps: ps["score"])
  return max_score.get("player")


def highest_card_wins(players: list):  
  highest_cards = [player.highest_card() for player in players]
  draw = helpers.all_in_list_same(highest_cards)
  if draw:
    return None
  return max(players, key = lambda player: player.highest_card())
 

def most_of_one_number_wins(players: list):
  return max_score_rule(
    players,
    lambda player: player.palette.get_one_number_cards_number()
  )


def most_of_one_color_wins(players: list):
  return max_score_rule(
    players,
    lambda player: player.palette.get_one_color_cards_number()
  )


def most_even_cards_wins(players: list):
  return max_score_rule(
    players,
    lambda player: player.palette.get_even_cards_number()
  )


def most_different_colors_win(players: list):
  return max_score_rule(
    players,
    lambda player: player.palette.get_different_colors_card_number()
  )


def most_cards_below_4_wins(players: list):
  return max_score_rule(
    players,
    lambda player: player.palette.get_less_then_4_cards_number()
  )


def most_cards_in_a_row_wins(players: list):
  return max_score_rule(
    players,
    lambda player: player.palette.get_largest_order_of_cards()
  )
