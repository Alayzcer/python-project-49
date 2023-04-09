import random


DESCRIPTION = ('Answer "yes" if the number '
               'is even, otherwise answer "no".')


def make_step():
    random_number = random.randrange(1, 345)
    question = str(random_number)
    no_is_even = random_number % 2 == 0
    answer = "yes" if no_is_even else "no"
    return [question, answer]
