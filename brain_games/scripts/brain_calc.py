from brain_games.brain_games.calc import generate_round
from brain_games.engine import run_game


def main():
    instruction = 'What is the result of the expression?'
    run_game(generate_round, instruction)

if __name__ == "__main__":
    main()
