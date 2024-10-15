from copy import deepcopy
import numpy as np

from rlcard.games.euchre import Dealer
from rlcard.games.euchre import Player
from rlcard.games.euchre import Judger

class EuchreGame:

    def __init__(self, allow_step_back=False) -> None:
        self.allow_step_back = allow_step_back
        self.np_random = np.random.RandomState()
        # hardcoded, but attributes specified to ensure compatibility with existing code
        self.num_players = 4
        self.num_decks = 1
        self.game_pointer = 0
        self.tricks = []
        self.trump = None
        self.turn_up = None
        self.current_trick = None

    def init_game(self) -> tuple[dict, int]:
        self.tricks = [0,0]
        self.dealer = Dealer(self.np_random)
        self.judger = Judger(self.np_random)
        self.players = []
        self.current_trick = []
        for i in range(self.num_players):
            self.players.append(Player(i, self.np_random))
        
        # deal out a hand to each player, alternate two's and three's like in euchre
        a = 0
        for i in range(self.num_players):
            self.dealer.deal_card(self.players[i],2+(a&1))
            a += 1
        a = 1
        for i in range(self.num_players):
            self.dealer.deal_card(self.players[i],2+(a&1))
            a += 1
        self.turn_up = self.dealer.flip_card()
        self.trump = self.turn_up.suit
        # for player in self.players:
        #     print(player.show_hand())
    
        state = self.get_state(self.game_pointer)

        return state, self.game_pointer
        
    def step(self, action) -> tuple[dict, int]:

        # Action # will match the index of the card in the player's hand
        # TODO step back

        next_state = {}

        player = self.players[self.game_pointer]
        card = player.play_card(action)


    def get_state(self, player) -> dict:
        tricks = [self.tricks[player.team], self.tricks[(player.team+1)%2]]
        state = self.players[player].get_state(tricks, self.turn_up, self.current_trick)
        state['current_player'] = self.game_pointer
        return state

    def is_over(self) -> bool:
        return sum(self.tricks) >= 5

    def get_payoffs(self) -> list[int]:
        ''' Return the payoffs of the game

        Returns:
            (list): Each entry corresponds to the payoff of one player
        '''
        # TODO counts first team as callers always, implement otherwise
        payoffs = [0,0,0,0]
        for t in self.tricks:
            if t == 5:
                payoffs[0] = 2
                payoffs[2] = 2

                payoffs[1] = 0
                payoffs[3] = 0
            elif t >= 3:
                payoffs[0] = 1
                payoffs[2] = 1

                payoffs[1] = 0
                payoffs[3] = 0
            else:
                payoffs[0] = 0
                payoffs[2] = 0

                payoffs[1] = 2
                payoffs[3] = 2
        return payoffs

