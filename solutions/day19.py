from textwrap import dedent
from io import StringIO

import functools


def parse(data):
    towels = list(data.readline().strip().split(', '))
    _ = data.readline()
    patterns = list(line.strip() for line in data.readlines())

    return towels, patterns


def part1(data):
    towels, patterns = parse(data)

    @functools.cache
    def matches(pattern):
        if not pattern:
            return True

        for towel in towels:
            if pattern.startswith(towel):
                if matches(pattern[len(towel):]):
                    return True

        return False

    return sum(1 for _ in filter(matches, patterns))


def part2(data):
    towels, patterns = parse(data)


    @functools.cache
    def matches(pattern):
        if not pattern:
            return 1

        x = 0
        for towel in towels:
            if pattern.startswith(towel):
                m = matches(pattern[len(towel):])
                x += m

        return x

    return sum(map(matches, patterns))



def test_part1():
    result = part1(StringIO(dedent('''\
        r, wr, b, g, bwu, rb, gb, br
        
        brwrr
        bggr
        gbbr
        rrbgbr
        ubwu
        bwurrg
        brgr
        bbrgwb
    ''')))

    assert result == 6


def test_part2():
    result = part2(StringIO(dedent('''\
        r, wr, b, g, bwu, rb, gb, br
        
        brwrr
        bggr
        gbbr
        rrbgbr
        ubwu
        bwurrg
        brgr
        bbrgwb
    ''')))

    assert result == 16

