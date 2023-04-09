import random


DESCRIPTION = ('Answer "yes" if the number '
               'is even, otherwise answer "no".')


def get_data_of_next_step():
    random_number = random.randrange(1, 345)
    question = str(random_number)
    answer = "yes" if random_number % 2 == 0 else "no"
    return [question, answer]
