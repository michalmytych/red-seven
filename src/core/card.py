from core.color import Color

class Card:
  def __init__(self, number: int, color: Color):
    self.number = number
    self.color = color

  def __repr__(self):
    return f'{self.color}:{self.number}'

  def __str__(self):
    return f'{self.color}:{self.number}'

  def __int__(self):
    return self.number

  def __mod__(self, other):
    return self.number % other

  def __lt__(self, card: object):
    number_is_smaller = self.number < card.number
    color_is_smaller = self.color < card.color
    return number_is_smaller or (self.numer == card.numer and color_is_smaller)

  def __gt__(self, card: object):
    number_is_bigger = self.number > card.number
    color_is_bigger = self.color > card.color
    return number_is_bigger or (self.numer == card.number and color_is_bigger)
