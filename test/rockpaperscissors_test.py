import unittest
from parameterized import parameterized

from rockpaperscissors import ROCK, SCISSORS, PAPER, PLAYER_ONE_WINS, PLAYER_TWO_WINS, play_round, DRAW, play_game


class RockPaperScissorsTest(unittest.TestCase):

    @parameterized.expand([
        (ROCK, SCISSORS, PLAYER_ONE_WINS),
        (SCISSORS, ROCK, PLAYER_TWO_WINS)
    ]
    )
    def test_rock_blunts_scissors(self, player1, player2, winner):
        self.assertEqual(winner, play_round(player1, player2))

    @parameterized.expand([
        (PAPER, ROCK, PLAYER_ONE_WINS),
        (ROCK, PAPER, PLAYER_TWO_WINS)
    ]
    )
    def test_paper_wraps_rock(self, player1, player2, winner):
        self.assertEqual(winner, play_round(player1, player2))

    @parameterized.expand([
        (SCISSORS, PAPER, PLAYER_ONE_WINS),
        (PAPER, SCISSORS, PLAYER_TWO_WINS)
    ]
    )
    def test_scissors_cut_paper(self, player1, player2, winner):
        self.assertEqual(winner, play_round(player1, player2))

    @parameterized.expand([
        (ROCK, ROCK, DRAW),
        (PAPER, PAPER, DRAW),
        (SCISSORS, SCISSORS, DRAW)
    ]
    )
    def test_draw_when_same(self, player1, player2, winner):
        self.assertEqual(winner, play_round(player1, player2))

    @parameterized.expand([
        (ROCK, SCISSORS, PLAYER_ONE_WINS),
        (PAPER, SCISSORS, PLAYER_TWO_WINS)
    ]
    )
    def test_first_player_with_two_points_wins_game(self, player1, player2, winner):
        self.assertEqual(winner, play_game([
            play_round(player1, player2),  # player 1 wins round
            play_round(player2, player1),  # player 2 wins round
            play_round(player1, player2)   # player 1 wins round
        ]))

    def test_draws_dont_count_in_game(self):
        self.assertEqual(None, play_game([
            play_round(ROCK, ROCK),
            play_round(ROCK, ROCK),
            play_round(ROCK, ROCK),
            play_round(ROCK, ROCK)
        ]))


if __name__ == '__main__':
    unittest.main()
