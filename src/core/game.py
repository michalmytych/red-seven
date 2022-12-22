from core.utils import generate_shuffled_deck


class Game:
  def __init__(self, id: int):
    self.id = id        
    self.offset = []
    self.players = []
    self.active_players = None
    self.deck = generate_shuffled_deck()

  def deal_seven_covered_cards(self):
    pass

  def deal_one_uncovered_card(self):
    pass

  def deal_starting_card(self):
    pass

  def select_starting_player(self):
    pass

  def next_player(self):
    pass

  def check_if_players_have_cards(self):
    pass

  def check_players_hands(self):
    pass

