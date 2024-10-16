from euchre_card import EuchreCard as Card
from trick import EuchreTrick as Trick
from player import EuchrePlayer as Player

class EuchreJudger:
    def __init__(self, np_random):
        self.np_random = np_random

    def judge_trick(self, trick: Trick, trump_suit: str) -> int:
        '''
        Take in a trick of cards (in order, lead card is first), and the trump suit from the game as input and return the player id of the winner of the trick
        '''
        cards = trick.get_cards()
        led_suit, player_ids = trick.get_led_suit(), trick.get_player_ids()
        winner, max_card = player_ids[0], cards[0]

        for i,c in enumerate(cards):
            trump_flag = 0
            rb_flag = 0
            lb_flag = 0

            higher_same_suit = c.get_suit() == led_suit and c.get_rank() > max_card.get_rank() and trump_flag == 0
            first_trump = c.get_suit() == trump_suit and trump_flag == 0
            higher_trump = c.get_suit() == trump_suit and trump_flag == 1 and c.get_rank() > max_card.get_rank() and lb_flag == 0 and rb_flag == 0
            
            if higher_same_suit or first_trump or higher_trump:
                winner = player_ids[i]
                max_card = c

            left_bower = c.get_suit_compliment() == trump_suit and c.get_rank() == 'J'
            if left_bower and rb_flag == 0:
                winner = player_ids[i]
                max_card = c
                lb_flag = 1
            right_bower = c.get_suit() == trump_suit and c.get_rank() == 'J'
            if right_bower:
                winner = player_ids[i]
                max_card = c
                rb_flag = 1
            trump_flag = rb_flag or lb_flag or first_trump or higher_trump

        return winner

    def judge_round(self, player: Player) -> dict[int, int]:
        ''' 
        Take in context of round (e.g. who 'called' trump) and return points for winning team based on tricks won
        '''
        pass