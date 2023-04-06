#!/usr/bin/env python3
from brain_games import game_cycle
from brain_games.games import progression


def main():
    game_cycle.run(progression.get_api())


if __name__ == '__main__':
    main()
