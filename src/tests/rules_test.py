import core.rules as rules
from core.player import Player
import core.utils as utils


deck = utils.generate_shuffled_deck()

def test_highest_card_wins_by_number():
  players = [
    Player(0, palette=[
      utils.get_card_by_color_and_number(deck, 6, "red")
    ]),
    Player(1, palette=[
      utils.get_card_by_color_and_number(deck, 7, "red")
    ]),
  ]
  winner = rules.highest_card_wins(players)
  assert winner.id == 1


def test_highest_card_wins_by_color():
  players = [
    Player(1, palette=[
      utils.get_card_by_color_and_number(deck, 7, "blue")
    ]),
    Player(2, palette=[
      utils.get_card_by_color_and_number(deck, 7, "red")
    ]),
  ]
  winner = rules.highest_card_wins(players)
  assert winner.id == 2


def test_highest_card_wins_draw():
  players = [
    Player(1, palette=[
      utils.get_card_by_color_and_number(deck, 7, "red")
    ]),
    Player(2, palette=[
      utils.get_card_by_color_and_number(deck, 7, "red")
    ]),
  ]
  winner = rules.highest_card_wins(players)
  assert winner == None


def test_most_of_one_number_wins_simple():
  players = [
    Player(1, palette=[
      utils.get_card_by_color_and_number(deck, 1, "red"),
      utils.get_card_by_color_and_number(deck, 7, "red")
    ]),
    Player(2, palette=[
      utils.get_card_by_color_and_number(deck, 7, "red"),
      utils.get_card_by_color_and_number(deck, 7, "red")
    ]),
  ]
  winner = rules.most_of_one_number_wins(players)
  assert winner.id == 2


def test_most_of_one_number_wins_different_colors():
  players = [
    Player(1, palette=[
      utils.get_card_by_color_and_number(deck, 7, "blue"),
      utils.get_card_by_color_and_number(deck, 2, "red")
    ]),
    Player(2, palette=[
      utils.get_card_by_color_and_number(deck, 1, "indigo"),
      utils.get_card_by_color_and_number(deck, 1, "yellow"),
      utils.get_card_by_color_and_number(deck, 3, "yellow")
    ]),
  ]
  winner = rules.most_of_one_number_wins(players)
  assert winner.id == 2


def test_most_of_one_number_wins_complicated():
  players = [
    Player(1, palette=[
      utils.get_card_by_color_and_number(deck, 7, "blue"),
      utils.get_card_by_color_and_number(deck, 7, "red"),
      utils.get_card_by_color_and_number(deck, 2, "yellow"),
      utils.get_card_by_color_and_number(deck, 2, "indigo"),        
    ]),
    Player(2, palette=[
      utils.get_card_by_color_and_number(deck, 3, "indigo"),
      utils.get_card_by_color_and_number(deck, 3, "yellow"),
      utils.get_card_by_color_and_number(deck, 3, "blue"),
    ]),
  ]
  winner = rules.most_of_one_number_wins(players)
  assert winner.id == 2


def test_most_of_one_number_wins_draw_7_cards():
  players = [
    Player(1, palette=[
      utils.get_card_by_color_and_number(deck, 7, "blue"),
      utils.get_card_by_color_and_number(deck, 7, "red"),
      utils.get_card_by_color_and_number(deck, 7, "yellow"),
      utils.get_card_by_color_and_number(deck, 2, "indigo"),  
      utils.get_card_by_color_and_number(deck, 2, "yellow"),
      utils.get_card_by_color_and_number(deck, 2, "indigo"),       
      utils.get_card_by_color_and_number(deck, 1, "yellow"),       
    ]),
    Player(2, palette=[
      utils.get_card_by_color_and_number(deck, 3, "indigo"),
      utils.get_card_by_color_and_number(deck, 3, "yellow"),
      utils.get_card_by_color_and_number(deck, 3, "blue"),
      utils.get_card_by_color_and_number(deck, 2, "indigo"),
      utils.get_card_by_color_and_number(deck, 2, "yellow"),
      utils.get_card_by_color_and_number(deck, 2, "blue"),
      utils.get_card_by_color_and_number(deck, 4, "blue"),
    ]),
  ]
  winner = rules.most_of_one_number_wins(players)
  assert winner == None


def test_most_of_one_number_wins_draw():
  players = [
    Player(1, palette=[
      utils.get_card_by_color_and_number(deck, 7, "blue"),
      utils.get_card_by_color_and_number(deck, 7, "red"),
      utils.get_card_by_color_and_number(deck, 7, "red"),      
    ]),
    Player(2, palette=[
      utils.get_card_by_color_and_number(deck, 3, "indigo"),
      utils.get_card_by_color_and_number(deck, 3, "yellow"),
      utils.get_card_by_color_and_number(deck, 3, "blue"),
    ]),
  ]
  winner = rules.most_of_one_number_wins(players)
  assert winner == None


def test_most_of_one_color_wins_simple():
  players = [
    Player(1, palette=[
      utils.get_card_by_color_and_number(deck, 1, "blue"),
      utils.get_card_by_color_and_number(deck, 2, "red"),
      utils.get_card_by_color_and_number(deck, 3, "red"),      
    ]),
    Player(2, palette=[
      utils.get_card_by_color_and_number(deck, 1, "yellow"),
      utils.get_card_by_color_and_number(deck, 2, "yellow"),
      utils.get_card_by_color_and_number(deck, 3, "yellow"),
    ]),
  ]
  winner = rules.most_of_one_color_wins(players)
  assert winner.id == 2


def test_most_of_one_color_wins_complicated():
  players = [
    Player(1, palette=[
      utils.get_card_by_color_and_number(deck, 1, "yellow"),
      utils.get_card_by_color_and_number(deck, 2, "yellow"),
      utils.get_card_by_color_and_number(deck, 3, "red"), 
      utils.get_card_by_color_and_number(deck, 4, "red"),      
    ]),
    Player(2, palette=[
      utils.get_card_by_color_and_number(deck, 1, "green"),
      utils.get_card_by_color_and_number(deck, 2, "green"),
      utils.get_card_by_color_and_number(deck, 3, "green"),
    ]),
  ]
  winner = rules.most_of_one_color_wins(players)
  assert winner.id == 2


def test_most_of_one_color_wins_draw():
  players = [
    Player(1, palette=[
      utils.get_card_by_color_and_number(deck, 1, "yellow"),
      utils.get_card_by_color_and_number(deck, 2, "yellow"),
      utils.get_card_by_color_and_number(deck, 2, "red"),        
    ]),
    Player(2, palette=[
      utils.get_card_by_color_and_number(deck, 1, "green"),
      utils.get_card_by_color_and_number(deck, 2, "green"),
      utils.get_card_by_color_and_number(deck, 2, "yellow"),
    ]),
  ]
  winner = rules.most_of_one_color_wins(players)
  assert winner == None


def test_most_of_one_color_wins_draw_7_cards():
  players = [
    Player(1, palette=[
      utils.get_card_by_color_and_number(deck, 4, "indigo"),
      utils.get_card_by_color_and_number(deck, 2, "indigo"),
      utils.get_card_by_color_and_number(deck, 6, "indigo"),
      utils.get_card_by_color_and_number(deck, 3, "yellow"),
      utils.get_card_by_color_and_number(deck, 5, "yellow"),
      utils.get_card_by_color_and_number(deck, 2, "yellow"),
      utils.get_card_by_color_and_number(deck, 1, "red"),        
    ]),
    Player(2, palette=[
      utils.get_card_by_color_and_number(deck, 7, "green"),
      utils.get_card_by_color_and_number(deck, 7, "green"),
      utils.get_card_by_color_and_number(deck, 4, "green"),
      utils.get_card_by_color_and_number(deck, 5, "blue"),
      utils.get_card_by_color_and_number(deck, 3, "blue"),
      utils.get_card_by_color_and_number(deck, 1, "blue"),
      utils.get_card_by_color_and_number(deck, 2, "yellow"),
    ]),
  ]
  winner = rules.most_of_one_color_wins(players)
  assert winner == None
