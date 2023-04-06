#!/usr/bin/env python3
from brain_games import game_cycle
from brain_games.games import prime


def main():
    game_cycle.run(prime.get_api())


if __name__ == '__main__':
    main()
