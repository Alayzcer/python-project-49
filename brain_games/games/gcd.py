import random


def handle_gcd(a, b):
    a = abs(a)
    b = abs(b)
    if b > a:
        a, b = (b, a)
    while True:
        if 0 == b:
            return a
        a %= b
        if 0 == a:
            return b
        b %= a


def get_description():
    return 'Find the greatest common divisor of given numbers.'


def make_step():
    limit = 555
    a = random.randrange(1, limit)
    b = random.randrange(1, limit)
    question = f"{a} {b}"
    right_answer = handle_gcd(a, b)
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


def get_api():
    return {
        "get_description": get_description,
        "make_step": make_step,
        "get_question": get_question,
        "check_user_answer": check_user_answer,
        "get_right_answer": get_right_answer,
    }
