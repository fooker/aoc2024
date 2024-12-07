from textwrap import dedent
from io import StringIO
from itertools import product
from functools import reduce
from operator import add, mul


def process(data, ops):
    sum = 0

    for line in data:
        result, parts = line.split(': ')
        result = int(result)
        parts = list(map(int, parts.split(' ')))
        
        for sel in product(ops, repeat=len(parts)-1):
            if result == reduce(lambda a, b: b[1](a, b[0]),
                                zip(parts[1:], sel),
                                parts[0]):
                sum += result
                break

    return sum


def part1(data):
    return process(data, (add, mul))


def part2(data):
    ncc = lambda a, b: int('%s%s' % (a, b))
    return process(data, (add, mul, ncc))



def test_part1():
    result = part1(StringIO(dedent('''\
        190: 10 19
        3267: 81 40 27
        83: 17 5
        156: 15 6
        7290: 6 8 6 15
        161011: 16 10 13
        192: 17 8 14
        21037: 9 7 18 13
        292: 11 6 16 20
    ''')))

    assert result == 3749


def test_part2():
    result = part2(StringIO(dedent('''\
        190: 10 19
        3267: 81 40 27
        83: 17 5
        156: 15 6
        7290: 6 8 6 15
        161011: 16 10 13
        192: 17 8 14
        21037: 9 7 18 13
        292: 11 6 16 20
    ''')))

    assert result == 11387

