from euchre_card import EuchreCard as Card
from player import EuchrePlayer as Player
class EuchreTrick:

    def __init__(self):
        self.cards = []
        self.player_ids = []
        self.led_suit = None
        self.winner = None

    def add_card(self, player: Player, card: Card, trump_suit: str):
        '''
            Add a card to the trick. Corresponding list tracks whose card is whose.
            Set the led suit if it is the first card added.
        '''
        self.cards.append(card)
        self.player_ids.append(player.get_player_id())
        if self.led_suit is None:
            self.led_suit = card.get_suit(trump_suit)
    
    def get_cards(self):
        return self.cards
    
    def get_led_suit(self):
        return self.led_suit
    
    def get_player_ids(self):
        return self.player_ids
