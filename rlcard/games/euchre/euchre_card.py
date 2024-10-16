from rlcard.games.base import Card

class EuchreCard(Card):
    #TODO implement lookup index based on trump suit, fake 'suit' for left bower
    def __init__(self, suit, rank):
        super().__init__(suit, rank)

        # calculate power at trick-judging time based on trump suit
        self.power = None

    def __str__(self):
        return super().__str__()

    def __eq__(self, other):
        return super().__eq__(other)

    def __hash__(self):
        return super().__hash__()

    def get_index(self):
        return self.suit * 13 + self.rank

    def get_suit(self, trump_suit: str):
        if self.get_rank() == 'J' and self.get_suit_compliment() == trump_suit:
            return trump_suit
        else:
            return self.suit
    def get_rank(self):
        return self.rank
    
    def get_suit_compliment(self):
        '''
            Get the suit that is the same color as the current suit
        '''
        if self.suit == 'S':
            return 'H'
        elif self.suit == 'H':
            return 'S'
        elif self.suit == 'D':
            return 'C'
        elif self.suit == 'C':
            return 'D'
        