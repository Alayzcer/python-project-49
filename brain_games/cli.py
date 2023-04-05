import prompt


def get_user_name():
    name = prompt.string('May I have your name? ', False).strip()
    return name


def welcome_user():
    """ user's greeting
    """
    name = get_user_name()
    print(f"Hello, {name}!")
    return name


def get_user_answer_on_question(value):
    print("Question: ", value)
    answer = prompt.string('Your answer: ', False).strip()
    return answer
