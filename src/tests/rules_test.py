import core.rules as rules
from core.player import Player
from core.palette import Palette
from core.utils import card

def test_highest_card_wins_by_number():
  players = [
    Player(0, palette=Palette([
      card(6, "red")
    ])),
    Player(1, palette=Palette([
      card(7, "red")
    ])),
  ]
  winner = rules.highest_card_wins(players)
  assert winner.id == 1


def test_highest_card_wins_by_color():
  players = [
    Player(1, palette=Palette([
      card(7, "blue")
    ])),
    Player(2, palette=Palette([
      card(7, "red")
    ])),
  ]
  winner = rules.highest_card_wins(players)
  assert winner.id == 2


def test_highest_card_wins_draw():
  players = [
    Player(1, palette=Palette([
      card(7, "red")
    ])),
    Player(2, palette=Palette([
      card(7, "red")
    ])),
  ]
  winner = rules.highest_card_wins(players)
  assert winner == None


def test_most_of_one_number_wins_simple():
  players = [
    Player(1, palette=Palette([
      card(1, "red"),
      card(7, "red")
    ])),
    Player(2, palette=Palette([
      card(7, "red"),
      card(7, "red")
    ])),
  ]
  winner = rules.most_of_one_number_wins(players)
  assert winner.id == 2


def test_most_of_one_number_wins_different_colors():
  players = [
    Player(1, palette=Palette([
      card(7, "blue"),
      card(2, "red")
    ])),
    Player(2, palette=Palette([
      card(1, "indigo"),
      card(1, "yellow"),
      card(3, "yellow")
    ])),
  ]
  winner = rules.most_of_one_number_wins(players)
  assert winner.id == 2


def test_most_of_one_number_wins_complicated():
  players = [
    Player(1, palette=Palette([
      card(7, "blue"),
      card(7, "red"),
      card(2, "yellow"),
      card(2, "indigo"),        
    ])),
    Player(2, palette=Palette([
      card(3, "indigo"),
      card(3, "yellow"),
      card(3, "blue"),
    ])),
  ]
  winner = rules.most_of_one_number_wins(players)
  assert winner.id == 2


def test_most_of_one_number_wins_draw_7_cards():
  players = [
    Player(1, palette=Palette([
      card(7, "blue"),
      card(7, "red"),
      card(7, "yellow"),
      card(2, "indigo"),  
      card(2, "yellow"),
      card(2, "indigo"),       
      card(1, "yellow"),       
    ])),
    Player(2, palette=Palette([
      card(3, "indigo"),
      card(3, "yellow"),
      card(3, "blue"),
      card(2, "indigo"),
      card(2, "yellow"),
      card(2, "blue"),
      card(4, "blue"),
    ])),
  ]
  winner = rules.most_of_one_number_wins(players)
  assert winner == None


def test_most_of_one_number_wins_draw():
  players = [
    Player(1, palette=Palette([
      card(7, "blue"),
      card(7, "red"),
      card(7, "red"),      
    ])),
    Player(2, palette=Palette([
      card(3, "indigo"),
      card(3, "yellow"),
      card(3, "blue"),
    ])),
  ]
  winner = rules.most_of_one_number_wins(players)
  assert winner == None


def test_most_of_one_color_wins_simple():
  players = [
    Player(1, palette=Palette([
      card(1, "blue"),
      card(2, "red"),
      card(3, "red"),      
    ])),
    Player(2, palette=Palette([
      card(1, "yellow"),
      card(2, "yellow"),
      card(3, "yellow"),
    ])),
  ]
  winner = rules.most_of_one_color_wins(players)
  assert winner.id == 2


def test_most_of_one_color_wins_complicated():
  players = [
    Player(1, palette=Palette([
      card(1, "yellow"),
      card(2, "yellow"),
      card(3, "red"), 
      card(4, "red"),      
    ])),
    Player(2, palette=Palette([
      card(1, "green"),
      card(2, "green"),
      card(3, "green"),
    ])),
  ]
  winner = rules.most_of_one_color_wins(players)
  assert winner.id == 2


def test_most_of_one_color_wins_draw():
  players = [
    Player(1, palette=Palette([
      card(1, "yellow"),
      card(2, "yellow"),
      card(2, "red"),        
    ])),
    Player(2, palette=Palette([
      card(1, "green"),
      card(2, "green"),
      card(2, "yellow"),
    ])),
  ]
  winner = rules.most_of_one_color_wins(players)
  assert winner == None


def test_most_of_one_color_wins_draw_7_cards():
  players = [
    Player(1, palette=Palette([
      card(4, "indigo"),
      card(2, "indigo"),
      card(6, "indigo"),
      card(3, "yellow"),
      card(5, "yellow"),
      card(2, "yellow"),
      card(1, "red"),        
    ])),
    Player(2, palette=Palette([
      card(7, "green"),
      card(7, "green"),
      card(4, "green"),
      card(5, "blue"),
      card(3, "blue"),
      card(1, "blue"),
      card(2, "yellow"),
    ])),
  ]
  winner = rules.most_of_one_color_wins(players)
  assert winner == None


def test_most_even_cards_wins_simple():
  players = [
    Player(1, palette=Palette([
      card(1, "yellow"),
      card(2, "yellow"),
      card(3, "red"),        
    ])),
    Player(2, palette=Palette([
      card(1, "green"),
      card(4, "green"),
      card(6, "yellow"),
    ])),
  ]
  winner = rules.most_even_cards_wins(players)
  assert winner.id == 2


def test_most_even_cards_wins_complicated():
  players = [
    Player(1, palette=Palette([
      card(1, "yellow"),
      card(2, "red"),
      card(2, "red"),
    ])),
    Player(2, palette=Palette([
      card(2, "green"),
      card(4, "green"),
      card(6, "yellow"),
    ])),
  ]
  winner = rules.most_even_cards_wins(players)
  assert winner.id == 2


def test_most_even_cards_wins_draw():
  players = [
    Player(1, palette=Palette([
      card(2, "yellow"),
      card(2, "red"),
      card(2, "indigo"),
    ])),
    Player(2, palette=Palette([
      card(2, "green"),
      card(4, "green"),
      card(6, "yellow"),
    ])),
  ]
  winner = rules.most_even_cards_wins(players)
  assert winner == None


def test_most_different_colors_wins_draw():
  players = [
    Player(1, palette=Palette([
      card(1, "yellow"),
      card(2, "yellow"),
      card(3, "yellow"),
    ])),
    Player(2, palette=Palette([
      card(4, "yellow"),
      card(5, "yellow"),
      card(6, "red"),
    ])),
  ]
  winner = rules.most_different_colors_win(players)
  assert winner.id == 2


def test_most_different_colors_wins_draw():
  players = [
    Player(1, palette=Palette([
      card(1, "yellow"),
      card(2, "yellow"),
      card(3, "yellow"),
    ])),
    Player(2, palette=Palette([
      card(4, "yellow"),
      card(5, "yellow"),
      card(6, "yellow"),
    ])),
  ]
  winner = rules.most_different_colors_win(players)
  assert winner == None


def test_most_cards_below_4_wins_simple():
  players = [
    Player(1, palette=Palette([
      card(1, "yellow"),
      card(2, "indigo"),
      card(3, "indigo"),
    ])),
    Player(2, palette=Palette([
      card(4, "yellow"),
      card(1, "red"),
      card(1, "indigo"),
    ])),
  ]
  winner = rules.most_cards_below_4_wins(players)
  assert winner.id == 1


def test_most_cards_below_4_wins_draw():
  players = [
    Player(1, palette=Palette([
      card(1, "yellow"),
      card(2, "indigo"),
      card(3, "indigo"),
    ])),
    Player(2, palette=Palette([
      card(1, "indigo"),
      card(2, "green"),
      card(3, "yellow"),
    ])),
  ]
  winner = rules.most_cards_below_4_wins(players)
  assert winner == None


def test_most_cards_below_4_wins_draw():
  players = [
    Player(1, palette=Palette([
      card(1, "yellow"),
      card(2, "indigo"),
      card(3, "indigo"),
    ])),
    Player(2, palette=Palette([
      card(1, "indigo"),
      card(2, "green"),
      card(3, "yellow"),
    ])),
  ]
  winner = rules.most_cards_below_4_wins(players)
  assert winner == None


def test_most_cards_in_a_row_wins_simple():
  players = [
    Player(1, palette=Palette([
      card(1, "yellow"),
      card(2, "yellow"),
      card(3, "yellow"),
    ])),
    Player(2, palette=Palette([
      card(1, "green"),
      card(2, "green"),
      card(4, "green"),
    ])),
  ]
  winner = rules.most_cards_in_a_row_wins(players)
  assert winner.id == 1


def test_most_cards_in_a_row_wins_draw():
  players = [
    Player(1, palette=Palette([
      card(1, "yellow"),
      card(2, "yellow"),
      card(3, "yellow"),
    ])),
    Player(2, palette=Palette([
      card(4, "green"),
      card(5, "green"),
      card(6, "green"),
    ])),
  ]
  winner = rules.most_cards_in_a_row_wins(players)
  assert winner == None
