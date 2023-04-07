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
    answer = handle_gcd(a, b)
    return [question, str(answer)]
