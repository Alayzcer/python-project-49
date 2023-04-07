import random


NUMBERS_RANGE_LIMIT = 345


def even_to_str(value):
    is_even = value % 2 == 0
    return "yes" if is_even else "no"


def get_description():
    return ('Answer "yes" if the number '
            'is even, otherwise answer "no".')


def make_step():
    no = random.randrange(1, NUMBERS_RANGE_LIMIT)
    question = str(no)
    answer = even_to_str(no)
    return [question, answer]
