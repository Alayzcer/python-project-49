import random


DESCRIPTION = 'What number is missing in the progression?'


def make_sequence(length, first, step_by):
    """ create arithmetic sequence
    """
    res = [first]
    for i in range(length - 1):
        last = res[i]
        res.append(last + step_by)
    return res


def get_data_of_next_step():
    min_range = 5
    max_range = 15
    first = random.randrange(1, 555)
    step_by = random.randrange(1, 55)
    elements_count = random.randrange(min_range, max_range)
    random_id = random.randrange(1, elements_count)
    numbers_sequence = make_sequence(elements_count, first, step_by)
    answer = numbers_sequence[random_id]
    numbers_sequence[random_id] = ".."
    question = " ".join(map(str, numbers_sequence))
    return [question, str(answer)]
