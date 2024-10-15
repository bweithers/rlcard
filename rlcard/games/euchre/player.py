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

    def get_player_id(self):
        ''' Return player's id
        '''
        return self.player_id
    
    def show_hand(self):
        return [str(card) for card in self.hand]
    
    def play_card(self, card_idx):
        card = self.hand[card_idx]
        self.hand.remove(card)
        return card

    def get_legal_actions(self, current_trick):
        # TODO are actions index of card in hand or index of card from state?
        # TODO Left Bower Suit Nonsense
        legal_actions = []
        for i in range(len(self.hand)):
            if self.hand[i].suit == current_trick.suit:
                legal_actions.append(i)
        return legal_actions
    
    def get_state(self, tricks, turn_up, current_trick):
        # TODO implement state
        state = {}
        state['hand'] = self.hand.get_index()
        state['tricks'] = tricks
        state['trump'] = turn_up.suit
        state['turn_up'] = turn_up
        state['current_trick'] = current_trick
        state['legal_actions'] = self.get_legal_actions(current_trick)
        return state
