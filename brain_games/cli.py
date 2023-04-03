import prompt


def welcome_user():
    """ user's greeting
    """
    while True:
        name = prompt.string('May I have your name? ').strip()
        # skip only spaces
        if 0 == len(name):
            continue
        print(f"Hello, {name}!")
        break
