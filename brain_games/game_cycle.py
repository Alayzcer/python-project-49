import prompt


GAME_STEPS_COUNT = 3


def run(game):
    """ invoke game  cycle
    """
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f"Hello, {user_name}!")
    print(game.DESCRIPTION)
    for _ in range(GAME_STEPS_COUNT):
        question, right_answer = game.get_data_of_next_step()
        print("Question:", question)
        user_answer = prompt.string('Your answer: ')
        if right_answer != user_answer:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{right_answer}'.")
            print(f"Let's try again, {user_name}!")
            break
        print("Correct!")
    else:
        print(f"Congratulations, {user_name}!")
