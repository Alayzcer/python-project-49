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
    op_id = random.randrange(0, len(OPERATORS))
    operator_name, operator_fn = OPERATORS[op_id]
    a = random.randrange(1, 30)
    b = random.randrange(1, 30)
    question = f"{a} {operator_name} {b}"
    answer = operator_fn(a, b)
    return [question, str(answer)]
