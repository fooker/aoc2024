from textwrap import dedent
from io import StringIO


def part1(data):
    l, r = zip(*(map(int, line.split()) for line in data))
    return sum(abs(l - r)  for (l, r) in zip(sorted(l), sorted(r)))


def part2(data):
    l, r = zip(*(map(int, line.split()) for line in data))
    return sum(x * r.count(x) for x in l)



def test_part1():
    result = part1(StringIO(dedent('''\
        3   4
        4   3
        2   5
        1   3
        3   9
        3   3
    ''')))

    assert result == 11


def test_part2():
    result = part2(StringIO(dedent('''\
        3   4
        4   3
        2   5
        1   3
        3   9
        3   3
    ''')))

    assert result == 31

