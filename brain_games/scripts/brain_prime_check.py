#!/usr/bin/env python3
from brain_games.games import prime


def make_test_data():
    return [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
            47, 53, 59, 61, 67, 71, 1523, 1531, 1543, 1549,
            1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601,
            1607, 1609, 1613, 1619, 1621, 1627, ]


def check_implementation_on_data(content):
    res = map(prime.is_prime, content)
    return all(res)


def check_implementation():
    content = make_test_data()
    res = check_implementation_on_data(content)
    if res:
        print("all ok.")
    else:
        print("test failed")


def main():
    check_implementation()


if __name__ == '__main__':
    main()
