from copy import deepcopy
import numpy as np

from rlcard.games.euchre import Dealer
from rlcard.games.euchre import Player
from rlcard.games.euchre import Judger

class EuchreGame:

    def __init__(self, allow_step_back=False):
        self.allow_step_back = allow_step_back
        self.np_random = np.random.RandomState()
        # hardcoded, but attributes specified to ensure compatibility with existing code
        self.num_players = 4
        self.num_decks = 1

    def init_game(self):
        self.dealer = Dealer(self.np_random)
        self.judger = Judger(self.np_random)
        self.players = []
        for i in range(self.num_players):
            self.players.append(Player(i, self.np_random))
        
        a = 0
        for i in range(self.num_players):
            self.dealer.deal_card(self.players[i],2+(a&1))
            a += 1
        a = 1
        for i in range(self.num_players):
            self.dealer.deal_card(self.players[i],2+(a&1))
            a += 1

            
        print(self.players[0].hand)
        print(self.players[1].hand)
        print(self.players[2].hand)
        print(self.players[3].hand)
            