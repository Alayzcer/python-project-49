#!/usr/bin/env python3
import random
import prompt
from brain_games import cli


QUESTION_NUMBER_LIMIT = 255
GAME_STEPS_COUNT = 3


def get_right_answer(value: int) -> str:
    is_even = value % 2 == 0
    return "yes" if is_even else "no"


def game_step():
    number = random.randrange(1, QUESTION_NUMBER_LIMIT)
    right_answer = get_right_answer(number)
    user_answer = prompt.string(f"Question: {number}\n").strip().lower()
    check = user_answer == right_answer
    if check:
        print("Correct!")
    else:
        print(f"'{user_answer}' is wrong answer ;(. "
              f"Correct answer was '{right_answer}'.")
    return check


def main():
    print("Welcome to the Brain Games!")
    user_name = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(GAME_STEPS_COUNT):
        answer_is_not_right = not game_step()
        if answer_is_not_right:
            print(f"Let's try again, {user_name}")
            return
    print(f"Congratulations, {user_name}!")


if __name__ == '__main__':
    main()
