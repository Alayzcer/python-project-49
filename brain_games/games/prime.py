import random


def is_prime(value):
    if value <= 1:
        return False
    if 2 == value:
        return True
    for i in range(3, value):
        if 0 == value % i:
            return False
    return True


def prime_int_to_str(value):
    return "yes" if is_prime(value) else "no"


def get_description():
    return ('Answer "yes" if given number '
            'is prime. Otherwise answer "no".')


def make_step():
    limit = 111
    value = random.randrange(3, limit)
    answer = prime_int_to_str(value)
    return {
        "question": str(value),
        "right_answer": answer,
    }


def get_question(step):
    return step["question"]


def check_user_answer(step, user_answer):
    return user_answer.lower() == step["right_answer"]


def get_right_answer(step):
    return step["right_answer"]


def get_api():
    return {
        "get_description": get_description,
        "make_step": make_step,
        "get_question": get_question,
        "check_user_answer": check_user_answer,
        "get_right_answer": get_right_answer,
    }
