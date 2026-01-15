from brain_games.cli import welcome_user


def run_game(game_logic, instructions):
    name = welcome_user()
    print(instructions)

    total_rounds = 3

    for _ in range(total_rounds):
        question, correct_answer = game_logic()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if str(user_answer).strip() == str(correct_answer):
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' Is wrong answer ;(. The correct answer was {correct_answer}.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
