#!/usr/bin/env python3
import random
from brain_games import game_cycle


def get_description():
    return 'What number is missing in the progression?'


def make_sequence(len, first, step_by):
    res = [first]
    for i in range(len - 1):
        last = res[i]
        res.append(last + step_by)


def make_step():
    min_range = 5
    max_range = 15
    limit = 55
    first = random.randrange(1, 555)
    step_by = random.randrange(1, limit)
    elements_count = random.randrange(min_range, max_range)
    random_id = random.randrange(1, elements_count)
    seq = make_sequence(elements_count, first, step_by)
    hidden_elem = seq[random_id]
    seq[random_id] = ".."
    question = " ".join(seq)
    return {
        "question": question,
        "right_answer": hidden_elem,
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
