from brain_games.cli import welcome_user
import random


def is_even():
    name = welcome_user()

    print('Answer "even" if the number is even, otherwise answer "odd".')

    correct_followed = 0

    while correct_followed < 3:
        number = random.randint(1, 100)

        print(f'Question: {number}')

        answer = input('Your answer: ').strip().lower()

        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        if answer == correct_answer:
            print('Correct!')
            correct_followed += 1

        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')


if __name__ == "__main__":
    is_even()
