from textwrap import dedent
from io import StringIO
from dataclasses import dataclass

import math
import functools

@functools.cache
def evolve(n, val):
    if n == 0:
        return 1
    else:
        n = n - 1

    if val == 0:
        return evolve(n, 1)

    digits = int(math.log10(val)) + 1
    if digits % 2 == 0:
        return evolve(n, val // (10**(digits//2))) + \
               evolve(n, val %  (10**(digits//2)))

    return evolve(n, val * 2024)


def part1(data):
    data = data.read()
    data = map(int, data.split(' '))

    return sum(evolve(25, val) for val in data)


def part2(data):
    data = data.read()
    data = map(int, data.split(' '))

    return sum(evolve(75, val) for val in data)


def test_evolve():
    assert evolve(0, 99) == 1

    assert evolve(1, 0) == 1
    assert evolve(1, 1) == 1

    assert evolve(1, 10) == 2

    assert evolve(1, 1122) == 2
    assert evolve(2, 1122) == 4

    assert evolve(6, 17) == 15


def test_part1():
    result = part1(StringIO('125 17'))

    assert result == 55312

