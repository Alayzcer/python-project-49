import math
import random


DESCRIPTION = ('Answer "yes" if given number '
               'is prime. Otherwise answer "no".')


def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True


def get_data_of_next_step():
    question = random.randrange(3, 111)
    answer = "yes" if is_prime(question) else "no"
    return [str(question), answer]
