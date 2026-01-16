from brain_games.cli import welcome_user
import random


def generate_progression():
    length = random.randint(5, 10)
    start = random.randint(1, 20)
    step = random.randint(1, 10)

    progression = []

    for i in range(length):
        progression.append(str(start + i * step))

    hidden_index = random.randint(0, length - 1)

    correct_answer = progression[hidden_index]

    progression[hidden_index] = '..'

    return ' '.join(progression), correct_answer


def play_progression():
    name = welcome_user()

    print("What number is missing in the progression?")

    rounds_to_win = 3

    for _ in range(rounds_to_win):
        progression, correct_answer = generate_progression()

        print(f"Question: {progression}")

        user_answer = input("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")

        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")

            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    play_progression()
