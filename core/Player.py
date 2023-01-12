from uuid import uuid4
from core.Hand import Hand
from core.Palette import Palette


class Player:

    def __init__(self):
        id = str(uuid4())
        self.id = id
        self.hand = Hand()
        self.palette = Palette()
        self.active = True
        print(f'Initalized Player {id}')

    def serialize(self):
      return {
        "id": self.id,
        "hand": self.hand.serialize(),
        "palette": self.palette.serialize(),
        "active": self.active
      }

    def __repr__(self):
        return f'Player[id={self.id}]'

    def set_card_to_canvas(self, index, canvas):
        self.hand.set_card_to_canvas(index, canvas)

    def set_card_to_palette(self, index):
        self.hand.set_card_to_palette(index, self.palette)
        self.hand.sort()
        self.palette.sort()

    def display_player_desk(self, game, player_number):
        self.hand.sort()
        game.display_desk()
        # zaaktualizuj widok desku gry
        # wyślij do gracza widok jego ręki
        print(f'Your({player_number + 1} player) hand: ')
        for num, card in enumerate(self.hand.cards):
            print(f'{num + 1}: {card}')

    def run_turn(self, game, player_number, canvas):
        self.display_player_desk(game, player_number)
        # wyślij do gracza widok jego palety
        answer = input('Do you want set card to canvas(y/n): ')
        # daj czas graczowi na wybór czy chce zagrać na canvas i jeśli tak to ile kart
        if answer.lower() == 'y':
            card_number = input('Select number of card you want to set to canvas: ')
            self.set_card_to_canvas(int(card_number)-1, canvas)
            self.display_player_desk(game, player_number)
        answer = input('Do you want set card to palette(y/n): ')
        # daj czas graczowi na wybór czy chce pociągną do palety i jeśli tak to ile kart
        if answer.lower() == 'y':
            card_number = input('Select number of card you want to set to palette: ')
            self.set_card_to_palette(int(card_number)-1)
            self.display_player_desk(game, player_number)
