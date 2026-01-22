from brain_games.engine import run_game
from brain_games.games import even


def main():
    run_game(even.instruction, even.get_round_data)


if __name__ == '__main__':
    main()
