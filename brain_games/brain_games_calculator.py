from brain_games.cli import welcome_user
import random


def calculator():
    name = welcome_user()
    
    print('What is the result of the expression?')

    correct_followed = 0

    while correct_followed < 3:
        num1 = random.randint(1, 25)
        num2 = random.randint(1, 10)
        operation = random.choice(['+', '-', '*'])
        
        question = f"{num1} {operation} {num2}"
        
        print(f'Question: {question}')

        if operation == '+':
            correct_answer = num1 + num2
        elif operation == '-':
            correct_answer = num1 - num2
        else: # operation == '*'
            correct_answer = num1 * num2

        answer = input('Your answer: ').strip()

        if answer == str(correct_answer):
            print('Correct!')
            correct_followed += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')

if __name__ == "__main__":
    calculator()
