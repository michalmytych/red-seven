import core.rules as rules

VERSION = "1.2"

COLORS = (
  (0, "red", rules.highest_card_wins),
  (1, "orange", rules.most_of_one_number_wins),
  (2, "yellow", rules.most_of_one_color_wins),
  (3, "green", rules.most_even_cards_wins),
  (4, "blue", rules.most_different_colors_wins),
  (5, "indigo", rules.most_cards_in_a_row_wins),
  (6, "violet", rules.most_cards_below_4_wins)
)
