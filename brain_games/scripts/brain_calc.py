#!/usr/bin/env python3
import random
from brain_games import game_cycle


OPERATORS = [
    ["+", lambda a, b: a + b],
    ["-", lambda a, b: a - b],
    ["*", lambda a, b: a * b],
]
OPERAND_LIMIT = 30


def get_description():
    return 'What is the result of the expression?'


def make_step():
    op_id = random.randrange(0, len(OPERATORS))
    a = random.randrange(1, OPERAND_LIMIT)
    b = random.randrange(1, OPERAND_LIMIT)
    question = f"{a} {OPERATORS[op_id][0]} {b}"
    right_answer = OPERATORS[op_id][1](a, b)
    return {
        "question": question,
        "right_answer": right_answer,
    }


def get_question(step):
    return step["question"]


def check_user_answer(step, user_answer):
    try:
        input = int(user_answer)
    except ValueError:
        return False
    return input == step["right_answer"]


def get_right_answer(step):
    return step["right_answer"]


def main():
    game_cycle.run({
        "get_description": get_description,
        "make_step": make_step,
        "get_question": get_question,
        "check_user_answer": check_user_answer,
        "get_right_answer": get_right_answer,
    })


if __name__ == '__main__':
    main()
