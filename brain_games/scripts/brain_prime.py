from brain_games.cli import welcome_user
import random


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
 
    return True


def play_prime():
    name = welcome_user()

    print("Answer 'yes' if given number is prime. Otherwise answer 'no'.")

    rounds_to_win = 3

    for _ in range(rounds_to_win):
        number = random.randint(1, 100)

        print(f"Question: {number}")

        correct_answer = 'yes' if is_prime(number) else 'no'

        user_answer = input("Your answer: ").strip().lower()

        if user_answer == correct_answer:
            print("Correct!")

        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    play_prime()
