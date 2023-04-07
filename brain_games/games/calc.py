import random


OPERATORS = [
    ["+", lambda a, b: a + b],
    ["-", lambda a, b: a - b],
    ["*", lambda a, b: a * b],
]
OPERAND_LIMIT = 30


def get_description():
    return 'What is the result of the expression?'


def make_step():
    """ It creates a question and a right answer
    """
    op_id = random.randrange(0, len(OPERATORS))
    name, just_do_it = OPERATORS[op_id]
    a = random.randrange(1, OPERAND_LIMIT)
    b = random.randrange(1, OPERAND_LIMIT)
    question = f"{a} {name} {b}"
    answer = just_do_it(a, b)
    return [question, answer]
