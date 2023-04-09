import random


DESCRIPTION = ('Answer "yes" if given number '
               'is prime. Otherwise answer "no".')


def is_prime(number):
    if number <= 1:
        return False
    if 2 == number:
        return True
    for i in range(3, number):
        if 0 == number % i:
            return False
    return True


def make_step():
    limit = 111
    question = random.randrange(3, limit)
    answer = "yes" if is_prime(question) else "no"
    return [str(question), answer]
