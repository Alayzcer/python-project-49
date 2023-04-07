#!/usr/bin/env python3
from brain_games import game_cycle
from brain_games.games import calc


def main():
    game_cycle.run(calc.get_description(), calc.make_step)


if __name__ == '__main__':
    main()
