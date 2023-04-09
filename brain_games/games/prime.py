import random

DESCRIPTION = ('Answer "yes" if given number '
               'is prime. Otherwise answer "no".')


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


def make_step():
    limit = 111
    question = random.randrange(3, limit)
    answer = prime_int_to_str(question)
    return [str(question), answer]
