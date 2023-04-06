#!/usr/bin/env python3
import random
import math
from brain_games.games import gcd


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
        calculated_result = gcd.handle_gcd(a, b)
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


def main():
    check_implementation()


if __name__ == '__main__':
    main()
