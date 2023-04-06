import random


def make_sequence(len, first, step_by):
    """ create arithmetic sequence
    """
    res = [first]
    for i in range(len - 1):
        last = res[i]
        res.append(last + step_by)
    return res


def get_description():
    return 'What number is missing in the progression?'


def make_step():
    min_range = 5
    max_range = 15
    limit = 55
    first = random.randrange(1, 555)
    step_by = random.randrange(1, limit)
    elements_count = random.randrange(min_range, max_range)
    random_id = random.randrange(1, elements_count)
    content = make_sequence(elements_count, first, step_by)
    hidden_elem = content[random_id]
    content[random_id] = ".."
    question = " ".join(map(str, content))
    return {
        "question": question,
        "right_answer": hidden_elem,
    }


def get_question(step):
    return step["question"]


def check_user_answer(step, user_answer):
    try:
        input = int(user_answer)
    except ValueError:
        return False
    return input == step["right_answer"]


def get_right_answer(step):
    return step["right_answer"]


def get_api():
    return {
        "get_description": get_description,
        "make_step": make_step,
        "get_question": get_question,
        "check_user_answer": check_user_answer,
        "get_right_answer": get_right_answer,
    }
