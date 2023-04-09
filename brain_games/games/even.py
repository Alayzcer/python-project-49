import random


DESCRIPTION = ('Answer "yes" if the number '
               'is even, otherwise answer "no".')


def make_step():
    no = random.randrange(1, 345)
    question = str(no)
    no_is_even = no % 2 == 0
    answer = "yes" if no_is_even else "no"
    return [question, answer]
