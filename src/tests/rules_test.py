import core.rules as rules
from core.player import Player
from core.utils import card

def test_highest_card_wins_by_number():
  players = [
    Player(0, palette=[
      card(6, "red")
    ]),
    Player(1, palette=[
      card(7, "red")
    ]),
  ]
  winner = rules.highest_card_wins(players)
  assert winner.id == 1


def test_highest_card_wins_by_color():
  players = [
    Player(1, palette=[
      card(7, "blue")
    ]),
    Player(2, palette=[
      card(7, "red")
    ]),
  ]
  winner = rules.highest_card_wins(players)
  assert winner.id == 2


def test_highest_card_wins_draw():
  players = [
    Player(1, palette=[
      card(7, "red")
    ]),
    Player(2, palette=[
      card(7, "red")
    ]),
  ]
  winner = rules.highest_card_wins(players)
  assert winner == None


def test_most_of_one_number_wins_simple():
  players = [
    Player(1, palette=[
      card(1, "red"),
      card(7, "red")
    ]),
    Player(2, palette=[
      card(7, "red"),
      card(7, "red")
    ]),
  ]
  winner = rules.most_of_one_number_wins(players)
  assert winner.id == 2


def test_most_of_one_number_wins_different_colors():
  players = [
    Player(1, palette=[
      card(7, "blue"),
      card(2, "red")
    ]),
    Player(2, palette=[
      card(1, "indigo"),
      card(1, "yellow"),
      card(3, "yellow")
    ]),
  ]
  winner = rules.most_of_one_number_wins(players)
  assert winner.id == 2


def test_most_of_one_number_wins_complicated():
  players = [
    Player(1, palette=[
      card(7, "blue"),
      card(7, "red"),
      card(2, "yellow"),
      card(2, "indigo"),        
    ]),
    Player(2, palette=[
      card(3, "indigo"),
      card(3, "yellow"),
      card(3, "blue"),
    ]),
  ]
  winner = rules.most_of_one_number_wins(players)
  assert winner.id == 2


def test_most_of_one_number_wins_draw_7_cards():
  players = [
    Player(1, palette=[
      card(7, "blue"),
      card(7, "red"),
      card(7, "yellow"),
      card(2, "indigo"),  
      card(2, "yellow"),
      card(2, "indigo"),       
      card(1, "yellow"),       
    ]),
    Player(2, palette=[
      card(3, "indigo"),
      card(3, "yellow"),
      card(3, "blue"),
      card(2, "indigo"),
      card(2, "yellow"),
      card(2, "blue"),
      card(4, "blue"),
    ]),
  ]
  winner = rules.most_of_one_number_wins(players)
  assert winner == None


def test_most_of_one_number_wins_draw():
  players = [
    Player(1, palette=[
      card(7, "blue"),
      card(7, "red"),
      card(7, "red"),      
    ]),
    Player(2, palette=[
      card(3, "indigo"),
      card(3, "yellow"),
      card(3, "blue"),
    ]),
  ]
  winner = rules.most_of_one_number_wins(players)
  assert winner == None


def test_most_of_one_color_wins_simple():
  players = [
    Player(1, palette=[
      card(1, "blue"),
      card(2, "red"),
      card(3, "red"),      
    ]),
    Player(2, palette=[
      card(1, "yellow"),
      card(2, "yellow"),
      card(3, "yellow"),
    ]),
  ]
  winner = rules.most_of_one_color_wins(players)
  assert winner.id == 2


def test_most_of_one_color_wins_complicated():
  players = [
    Player(1, palette=[
      card(1, "yellow"),
      card(2, "yellow"),
      card(3, "red"), 
      card(4, "red"),      
    ]),
    Player(2, palette=[
      card(1, "green"),
      card(2, "green"),
      card(3, "green"),
    ]),
  ]
  winner = rules.most_of_one_color_wins(players)
  assert winner.id == 2


def test_most_of_one_color_wins_draw():
  players = [
    Player(1, palette=[
      card(1, "yellow"),
      card(2, "yellow"),
      card(2, "red"),        
    ]),
    Player(2, palette=[
      card(1, "green"),
      card(2, "green"),
      card(2, "yellow"),
    ]),
  ]
  winner = rules.most_of_one_color_wins(players)
  assert winner == None


def test_most_of_one_color_wins_draw_7_cards():
  players = [
    Player(1, palette=[
      card(4, "indigo"),
      card(2, "indigo"),
      card(6, "indigo"),
      card(3, "yellow"),
      card(5, "yellow"),
      card(2, "yellow"),
      card(1, "red"),        
    ]),
    Player(2, palette=[
      card(7, "green"),
      card(7, "green"),
      card(4, "green"),
      card(5, "blue"),
      card(3, "blue"),
      card(1, "blue"),
      card(2, "yellow"),
    ]),
  ]
  winner = rules.most_of_one_color_wins(players)
  assert winner == None
