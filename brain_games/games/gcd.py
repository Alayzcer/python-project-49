import random
import math


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


def make_test_data(limit, max_operand):
    res = [[25, 50, 25]]
    for i in range(limit):
        a = random.randrange(1, max_operand)
        b = random.randrange(1, max_operand)
        r = math.gcd(a, b)
        res.append([a, b, r])
    return res


def check_implementation_on_data(content):
    for it in content:
        a, b, result = it
        calculated_result = handle_gcd(a, b)
        if calculated_result != result:
            return [False, a, b, result, calculated_result]
    return [True]


def check_implementation():
    content = make_test_data(25, 789)
    res = check_implementation_on_data(content)
    if res[0]:
        print("all ok.")
    else:
        _, a, b, should, calc = res
        print(f"{a}, {b} should be {should}, but calculated {calc}")


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
