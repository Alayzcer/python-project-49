import random


NUMBERS_RANGE_LIMIT = 345


def even_to_str(value):
    is_even = value % 2 == 0
    return "yes" if is_even else "no"


def get_description():
    return ('Answer "yes" if the number '
            'is even, otherwise answer "no".')


def make_step():
    no = random.randrange(0, NUMBERS_RANGE_LIMIT)
    question = str(no)
    right_answer = even_to_str(no)
    return {
        "question": question,
        "right_answer": right_answer,
    }


def get_question(step):
    return step["question"]


def check_user_answer(step, user_answer):
    return user_answer.lower() == step["right_answer"]


def get_right_answer(step):
    return step["right_answer"]


def get_api():
    """ return functions of even game
    """
    return {
        "get_description": get_description,
        "make_step": make_step,
        "get_question": get_question,
        "check_user_answer": check_user_answer,
        "get_right_answer": get_right_answer,
    }
