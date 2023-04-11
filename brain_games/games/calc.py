import random

DESCRIPTION = 'What is the result of the expression?'
OPERATORS = [
    ["+", lambda a, b: a + b],
    ["-", lambda a, b: a - b],
    ["*", lambda a, b: a * b],
]


def get_data_of_next_step():
    """ It creates a question and a right answer
    """
    random_operator_id = random.randrange(0, len(OPERATORS))
    operator_name, operator_fn = OPERATORS[random_operator_id]
    a = random.randrange(1, 30)
    b = random.randrange(1, 30)
    question = f"{a} {operator_name} {b}"
    answer = operator_fn(a, b)
    return [question, str(answer)]
