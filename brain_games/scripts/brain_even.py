#!/usr/bin/env python3
import prompt
import random
from brain_games import cli


QUESTION_NUMBER_LIMIT = 255
GAME_STEPS_COUNT = 3


def right_answer(value: int) -> str:
    is_even = value % 2 == 0
    if is_even:
        return "yes"
    else:
        return "no"


def game_step() -> bool:
    number = random.randrange(1, QUESTION_NUMBER_LIMIT)
    user_answer = prompt.string(f"Question: {number}\n").strip().lower()
    return user_answer == right_answer(number)


def main():
    print("Welcome to the Brain Games!")
    user_name = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(GAME_STEPS_COUNT):
        answer_is_not_right = not game_step()
        if answer_is_not_right:
            print(f"Let's try again, {user_name}")
            return
        print("Correct!")
    print(f"Congratulations, {user_name}!")


if __name__ == '__main__':
    main()
