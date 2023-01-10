from collections import Counter
from core.config import CARDS_NUMBERS


class Palette:
    def __init__(self, cards: list = []):
        self.cards = cards

    def __str__(self):
        return_string = ''
        for card in self.cards:
            return_string += str(card)
        return return_string

    def sort(self):
        self.cards.sort(key=lambda x: (x.number, x.color), reverse=True)

    def get_one_color_cards_number(self):
        colors = Counter([card.color.strength for card in self.cards])
        return max(colors.values())

    def get_one_number_cards_number(self):
        numbers = Counter([card.number for card in self.cards])
        return max(numbers.values())

    def get_different_colors_card_number(self):
        colors = Counter([card.color.strength for card in self.cards])
        return len(colors.values())

    def get_even_cards_number(self):
        numbers = [card.number for card in self.cards if not card.number % 2]
        return len(numbers)

    def get_less_then_4_cards_number(self):
        numbers = [card.number for card in self.cards if card.number < 4]
        return len(numbers)

    def get_largest_order_of_cards(self):
        largest_order = 1
        order = 0
        numbers = [card.number for card in self.cards]
        for number in CARDS_NUMBERS:
            if number in numbers:
                order += 1
                if order > largest_order:
                    largest_order = order
            else:
                order = 0
        return largest_order
