from textwrap import dedent
from io import StringIO
from collections import defaultdict
from itertools import combinations

import numpy as np


def ck(p, map):
    return p[0] in range(map.shape[0]) and p[1] in range(map.shape[1])


def part1(data):
    map = np.array([list(line[:-1]) for line in data.readlines()])
    
    freqs = defaultdict(list)
    for idx, v in np.ndenumerate(map):
        if v != '.':
            freqs[v].append(idx)

    antinodes = set()
    for antennas in freqs.values():
        for a, b in combinations(antennas, 2):
            d = (a[0] - b[0], a[1] - b[1])
            n1 = (a[0] + d[0], a[1] + d[1])
            n2 = (b[0] - d[0], b[1] - d[1])

            if ck(n1, map):
                antinodes.add(n1)

            if ck(n2, map):
                antinodes.add(n2)

    return len(antinodes)


def part2(data):
    map = np.array([list(line[:-1]) for line in data.readlines()])
    
    freqs = defaultdict(list)
    for idx, v in np.ndenumerate(map):
        if v != '.':
            freqs[v].append(idx)

    antinodes = set()
    for antennas in freqs.values():
        for a, b in combinations(antennas, 2):
            d = (a[0] - b[0], a[1] - b[1])

            for i in range(1000):
                n1 = (a[0] + d[0] * i, a[1] + d[1] * i)
                n2 = (b[0] - d[0] * i, b[1] - d[1] * i)

                if ck(n1, map):
                    antinodes.add(n1)

                if ck(n2, map):
                    antinodes.add(n2)

                if not ck(n1, map) and not ck(n2, map):
                    break

    return len(antinodes)



def test_part1():
    result = part1(StringIO(dedent('''\
        ............
        ........0...
        .....0......
        .......0....
        ....0.......
        ......A.....
        ............
        ............
        ........A...
        .........A..
        ............
        ............
    ''')))

    assert result == 14


def test_part2():
    result = part2(StringIO(dedent('''\
        ............
        ........0...
        .....0......
        .......0....
        ....0.......
        ......A.....
        ............
        ............
        ........A...
        .........A..
        ............
        ............
    ''')))

    assert result == 34

