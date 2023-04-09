import random


DESCRIPTION = 'What number is missing in the progression?'


def make_sequence(len, first, step_by):
    """ create arithmetic sequence
    """
    res = [first]
    for i in range(len - 1):
        last = res[i]
        res.append(last + step_by)
    return res


def make_step():
    min_range = 5
    max_range = 15
    limit = 55
    first = random.randrange(1, 555)
    step_by = random.randrange(1, limit)
    elements_count = random.randrange(min_range, max_range)
    random_id = random.randrange(1, elements_count)
    content = make_sequence(elements_count, first, step_by)
    answer = content[random_id]
    content[random_id] = ".."
    question = " ".join(map(str, content))
    return [question, str(answer)]
