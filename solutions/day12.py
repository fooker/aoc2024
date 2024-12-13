from textwrap import dedent
from io import StringIO
from collections import defaultdict
from itertools import combinations

import numpy as np


def find_components(data):
    seen = set()
    components = defaultdict(set)

    label = 0

    for idx, v in np.ndenumerate(data):
        if idx in seen:
            continue

        stack = [ idx ]
        while stack:
            idx = stack.pop()
            if idx in seen:
                continue

            seen.add(idx)

            components[label].add(idx)

            for n in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nidx = (idx[0] + n[0], idx[1] + n[1])
                if nidx[0] not in range(data.shape[0]) or nidx[1] not in range(data.shape[1]):
                    continue
                
                if data[nidx] == v:
                    stack.append(nidx)

        label += 1

    return components


def part1(data):
    data = np.array([list(line[:-1]) for line in data.readlines()])
    components = find_components(data)

    result = 0
    for component in components.values():
        result += len(component) * (len(component) * 4 - sum(2 for a, b in combinations(component, 2) if (a[0] - b[0], a[1] - b[1]) in ((1, 0), (-1, 0), (0, 1), (0, -1))))

    return result


def part2(data):
    data = np.array([list(line[:-1]) for line in data.readlines()])
    components = find_components(data)

    result = 0
    for component in components.values():
        edges = 0
        for idx in component:
            for n in ((1, 1), (-1, 1), (1, -1), (-1, -1)):
                qidx = (idx[0] + n[0], idx[1] + n[1])
                nidx1 = (idx[0] + n[0], idx[1])
                nidx2 = (idx[0], idx[1] + n[1])
                if (nidx1 not in component) and (nidx2 not in component):
                    # Outer edge
                    edges += 1
                if (qidx not in component) and (nidx1 in component) and (nidx2 in component):
                    # Inner edge
                    edges += 1

        result += edges * len(component)

    return result



def test_part1():
    result = part1(StringIO(dedent('''\
        RRRRIICCFF
        RRRRIICCCF
        VVRRRCCFFF
        VVRCCCJFFF
        VVVVCJJCFE
        VVIVCCJJEE
        VVIIICJJEE
        MIIIIIJJEE
        MIIISIJEEE
        MMMISSJEEE
    ''')))

    assert result == 1930


def test_part2():
    result = part2(StringIO(dedent('''\
        RRRRIICCFF
        RRRRIICCCF
        VVRRRCCFFF
        VVRCCCJFFF
        VVVVCJJCFE
        VVIVCCJJEE
        VVIIICJJEE
        MIIIIIJJEE
        MIIISIJEEE
        MMMISSJEEE
    ''')))

    assert result == 1206

