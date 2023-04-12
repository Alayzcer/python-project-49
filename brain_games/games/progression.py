import random


DESCRIPTION = 'What number is missing in the progression?'


def generate_sequence(length, first, step_by):
    """ create arithmetic sequence
    """
    res = [first]
    for _ in range(length - 1):
        res.append(res[-1] + step_by)
    return res


def get_data_of_next_step():
    first = random.randrange(1, 555)
    step_by = random.randrange(1, 55)
    elements_count = random.randrange(5, 15)
    random_index = random.randrange(1, elements_count)
    numbers_sequence = generate_sequence(elements_count, first, step_by)
    answer = numbers_sequence[random_index]
    numbers_sequence[random_index] = ".."
    question = " ".join(map(str, numbers_sequence))
    return [question, str(answer)]
