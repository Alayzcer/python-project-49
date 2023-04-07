#!/usr/bin/env python3
from brain_games import game_cycle
from brain_games.games import even


def main():
    game_cycle.run(even.get_description(), even.make_step)


if __name__ == '__main__':
    main()
