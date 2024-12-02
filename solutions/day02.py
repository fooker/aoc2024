from textwrap import dedent
from io import StringIO
from itertools import pairwise


def check(report):
    monotonic = all(a - b < 0 for a, b in pairwise(report)) or all(a - b > 0 for a, b in pairwise(report))
    valid = all(0 < abs(a - b) <= 3 for a, b in pairwise(report))
    return monotonic and valid


def permute(report):
    for i in range(len(report) + 1):
        yield report[:i] + report[(i + 1):]


def part1(data):
    reports = (list(map(int, line.split())) for line in data)

    return sum(check(report) for report in reports)


def part2(data):
    reports = (list(map(int, line.split())) for line in data)

    return sum(any(check(tolerated) for tolerated in permute(report))
               for report
               in reports)



def test_part1():
    result = part1(StringIO(dedent('''\
        7 6 4 2 1
        1 2 7 8 9
        9 7 6 2 1
        1 3 2 4 5
        8 6 4 4 1
        1 3 6 7 9
    ''')))

    assert result == 2


def test_part2():
    result = part2(StringIO(dedent('''\
        7 6 4 2 1
        1 2 7 8 9
        9 7 6 2 1
        1 3 2 4 5
        8 6 4 4 1
        1 3 6 7 9
    ''')))

    assert result == 4

