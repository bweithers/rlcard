
class EuchreJudger:
    def __init__(self, np_random):
        self.np_random = np_random

    def judge_trick(self, trick, trump_suit) -> int:
        '''
        Take in a trick of cards (in order, lead card is first) and return the card index of the winning player of the trick
        '''
        pass

    def judge_round(self, player) -> dict[int, int]:
        ''' 
        Take in context of round (e.g. who 'called' trump) and return points for winning team based on tricks won
        '''
        pass

    def judge_game(self, game, game_pointer):
        pass