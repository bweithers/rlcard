from rlcard.games.base import Card

class EuchreCard(Card):
    #TODO implement lookup index based on trump suit, fake 'suit' for left bower
    def __init__(self, suit, rank):
        super().__init__(suit, rank)

    def __str__(self):
        return super().__str__()

    def __eq__(self, other):
        return super().__eq__(other)

    def __hash__(self):
        return super().__hash__()
