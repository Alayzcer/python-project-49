import prompt


def welcome_user():
    """ user's greeting
    """
    name = prompt.string('May I have your name? ', False).strip()
    print(f"Hello, {name}!")
