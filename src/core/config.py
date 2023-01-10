import core.rules as rules


VERSION = "1.2"

COLORS = (
  [0, "violet", rules.most_cards_below_4_wins],
  [1, "indigo", rules.most_cards_in_a_row_wins],
  [2, "blue", rules.most_different_colors_win],
  [3, "green", rules.most_even_cards_wins],
  [4, "yellow", rules.most_of_one_color_wins],
  [5, "orange", rules.most_of_one_number_wins],
  [6, "red", rules.highest_card_wins]
)

CARDS_NUMBERS = [1, 2, 3, 4, 5, 6, 7]
