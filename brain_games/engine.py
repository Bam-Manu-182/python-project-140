from brain_games.cli import welcome_user


def run_game(instruction, get_round_data):
    name = welcome_user()
    print(instruction)

    correct_answers = 0
    total_rounds = 3
    
    while correct_answers < total_rounds:
        question, correct_answer = get_round_data()
        print(f"Question: {question}")

        user_answer = input("Your answer: ")

        if user_answer == str(correct_answer):
            print("Correct!")
            correct_answers += 1

        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")

            return

    print(f"Congratulations, {name}!")
