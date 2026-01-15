from brain_games.cli import welcome_user
import random
import math


def get_gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2

    return num1


def play_gcd():
    name = welcome_user()

    print("Find the greatest common divisor of given numbers.")

    rounds_to_win = 3

    for _ in range(rounds_to_win):
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)

        print(f"Question: {number1} {number2}")

        correct_answer = get_gcd(number1, number2)

        user_answer = input("Your answer: ")

        if int(user_answer) == correct_answer:
            print("Correct!")

        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    play_gcd()
