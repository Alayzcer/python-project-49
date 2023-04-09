import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_gcd(a, b):
    a = abs(a)
    b = abs(b)
    if b > a:
        a, b = (b, a)
    while b != 0:
        n = a % b
        a = b
        b = n
    return a


def get_data_of_next_step():
    a = random.randrange(1, 555)
    b = random.randrange(1, 555)
    question = f"{a} {b}"
    answer = get_gcd(a, b)
    return [question, str(answer)]
