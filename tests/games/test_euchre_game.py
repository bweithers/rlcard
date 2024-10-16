import unittest

from rlcard.games.euchre.game import EuchreGame as Game
from rlcard.games.euchre.player import EuchrePlayer as Player

class TestEuchreMethods(unittest.TestCase):
    def test_get_num_players(self):
        game = Game()
        num_players = game.num_players
        self.assertEqual(num_players, 4)
    
    def test_init_game(self):
        game = Game()
        state, player_id = game.init_game()
        test_id = game.game_pointer
        self.assertEqual(test_id, player_id)
        print(state)
        