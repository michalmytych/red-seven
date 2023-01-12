class Card:

    DICT_OF_COLORS = {
        6: 'RED',
        5: 'ORANGE',
        4: 'YELLOW',
        3: 'GREEN',
        2: 'LIGHTBLUE',
        1: 'INDIGO',
        0: 'VIOLET'
    }
    LIST_OF_VALUES = [1, 2, 3, 4, 5, 6, 7]

    def __init__(self, color, value):
        self.color = Card.DICT_OF_COLORS[color]
        self.value = value

    def serialize(self):
      return {
        "color": self.color,
        "value": self.value,
      }

    def __str__(self):
        from Canvas import Canvas
        return f'{Card.DICT_OF_COLORS[self.color]} {self.value} Rule: {Canvas.RULES[self.color]}'
