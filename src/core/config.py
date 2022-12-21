import rules

VERSION = "1.2"

COLORS = (
  ("red", rules.highest_card_wins),
  ("orange", rules.most_of_one_number_wins),
  ("yellow", rules.most_of_one_color_wins),
  ("green", rules.most_even_cards_wins),
  ("blue", rules.most_different_colors_wins),
  ("indigo", rules.most_cards_in_a_row_wins),
  ("violet", rules.most_cards_below_4_wins)
)
