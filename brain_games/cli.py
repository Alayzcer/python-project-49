import prompt


def get_user_name():
    while True:
        name = prompt.string('May I have your name? ').strip()
        # skip only spaces
        if 0 == len(name):
            continue
        return name


def welcome_user():
    """ user's greeting
    """
    name = get_user_name()
    print(f"Hello, {name}!")
    return name


def get_user_answer_on_question(value):
    print(value)
    return prompt.string("Your answer: ").strip().lower()
