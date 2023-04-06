#!/usr/bin/env python3
from brain_games import game_cycle
from brain_games.games import gcd


def main():
    game_cycle.run(gcd.get_api())


if __name__ == '__main__':
    main()
