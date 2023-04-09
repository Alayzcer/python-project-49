#!/usr/bin/env python3
import prompt


GAME_STEPS_COUNT = 3


def run(core):
    """ invoke game cycle
    """
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ', False).strip()
    print(f"Hello, {user_name}!")
    print(core.DESCRIPTION)
    for _ in range(GAME_STEPS_COUNT):
        question, right_answer = core.make_step()
        print("Question:", question)
        user_answer = prompt.string('Your answer: ', False).strip().lower()
        if right_answer != user_answer:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{right_answer}'.")
            print(f"Let's try again, {user_name}!")
            break
    else:
        print("Correct!")
        print(f"Congratulations, {user_name}!")
