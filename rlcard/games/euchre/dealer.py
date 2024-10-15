import numpy as np
from rlcard.games.base import Card

class EuchreDealer:
    def __init__(self, np_random):
        self.np_random = np_random
        self.deck = [Card(suit, rank) for suit in ['S', 'H', 'D', 'C'] for rank in ['A', '9', 'T', 'J', 'Q', 'K']]
        self.shuffle()

    def shuffle(self):
        self.np_random.shuffle(self.deck)
        self.deck = list(self.deck)

    def deal_card(self, player, num_cards=1):
        for _ in range(num_cards):
            card = self.deck.pop()
            player.hand.append(card)

    def flip_card(self):
        return self.deck.pop()