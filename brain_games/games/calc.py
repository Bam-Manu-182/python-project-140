import random


def generate_round():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 10)

    operation = random.choice(['+', '-', '*'])

    question = f"{num1} {operation} {num2}"

    if operation == '+':
        answer = num1 + num2
    elif operation == '-':
        answer = num1 - num2
    else:  # operation == '*'
        answer = num1 * num2

    return question, answer
