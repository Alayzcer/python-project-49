#!/usr/bin/env python3
import random
from brain_games import game_cycle


def is_prime(value):
    if value <= 1:
        return False
    if 2 == value:
        return True
    for i in range(3, value):
        if 0 == value % i:
            return False
    return True


def make_test_data():
    content = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
               41, 43, 47, 53, 59, 61, 67, 71,
               1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579,
               1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657]
    return content


def check_implementation_on_data(content):
    res = map(is_prime, content)
    return all(res)


def check_implementation():
    content = make_test_data()
    res = check_implementation_on_data(content)
    if res:
        print("all ok.")
    else:
        print("test failed")


def prime_int_to_str(value):
    return "yes" if is_prime(value) else "no"


def get_description():
    return ('Answer "yes" if given number '
            'is prime. Otherwise answer "no".')


def make_step():
    limit = 55
    value = random.randrange(3, limit)
    answer = prime_int_to_str(value)
    return {
        "question": str(value),
        "right_answer": answer,
    }


def get_question(step):
    return step["question"]


def check_user_answer(step, user_answer):
    return user_answer == step["right_answer"]


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
