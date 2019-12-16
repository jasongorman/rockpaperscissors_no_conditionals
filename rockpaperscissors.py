PAPER = "paper"
SCISSORS = "scissors"
ROCK = "rock"

DRAW = 0
PLAYER_ONE_WINS = 1
PLAYER_TWO_WINS = 2


def play_round(player1, player2):
    return {
        ROCK: [ROCK, SCISSORS, PAPER],
        PAPER: [PAPER, ROCK, SCISSORS],
        SCISSORS: [SCISSORS, PAPER, ROCK]
    }[player1].index(player2)


def play_game(rounds):
    score = [0, 0, 0]

    for round_winner in rounds:
        score[round_winner] += 1
        try:
            return score[1:].index(2) + 1
        except ValueError:
            pass

    return None