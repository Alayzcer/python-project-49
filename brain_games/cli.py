import prompt


def welcome_user():
    """ user's greeting
    """
    name = prompt.string('May I have your name? ', False).strip()
    print(f"Hello, {name}!")
    return name


def get_user_answer_on_question(value):
    print("Question:", value.strip())
    answer = prompt.string('Your answer: ', False).strip()
    return answer
