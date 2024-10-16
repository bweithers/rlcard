from euchre_card import EuchreCard as Card
from trick import EuchreTrick as Trick

class EuchrePlayer:

    def __init__(self, player_id, np_random):
        ''' Initialize a Euchre player class

        Args:
            player_id (int): id for the player
        '''
        self.np_random = np_random
        self.player_id = player_id
        self.hand = []
        self.trick = 0
        self.team = player_id % 2

    def get_player_id(self) -> int:
        ''' Return player's id
        '''
        return self.player_id
    
    def show_hand(self) -> list[str]:    
        return [str(card) for card in self.hand]
    
    def play_card(self, card_idx) -> Card:
        card = self.hand[card_idx]
        self.hand.remove(card)
        return card

    def get_legal_actions(self, current_trick: Trick) -> list[int]:
        # TODO are actions index of card in hand or index of card from state?
        legal_actions = []
        # if we can follow suit, we must
        if any(card.get_suit() == current_trick.get_led_suit() for card in self.hand):
            legal_actions = [i for i in range(len(self.hand)) if self.hand[i].get_suit() == current_trick.get_led_suit()]
        # otherwise, we can play any card
        else:
            legal_actions = [i for i in range(len(self.hand))]
        return legal_actions
    
    def get_state(self, tricks: int, turn_up: Card, current_trick: Trick) -> dict:
        # TODO implement state
        state = {}
        state['hand'] = [card.get_index() for card in self.hand]
        state['tricks'] = tricks
        state['trump'] = turn_up.suit
        state['turn_up'] = turn_up
        state['current_trick'] = current_trick
        state['legal_actions'] = self.get_legal_actions(current_trick)
        return state
