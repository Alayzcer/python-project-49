#!/usr/bin/env python3
import prompt
from brain_games import cli


GAME_STEPS_COUNT = 3


def run(core):
    print("Welcome to the Brain Games!")
    user_name = cli.welcome_user()
    print(core["get_description"]())
    for _ in range(GAME_STEPS_COUNT):
        step = core["make_step"]()
        question = core["get_question"](step).strip()
        print("Question:", question)
        user_answer = prompt.string('Your answer: ', False).strip()
        if not core["check_user_answer"](step, user_answer):
            right_answer = core["get_right_answer"](step)
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{right_answer}'.")
            print(f"Let's try again, {user_name}!")
            return
        print("Correct!")
    print(f"Congratulations, {user_name}!")
