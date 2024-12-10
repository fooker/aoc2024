from textwrap import dedent
from io import StringIO

import numpy as np


def part1(data):
    data = np.array([list(map(int, line[:-1])) for line in data.readlines()])

    sum = 0

    for idx, v in np.ndenumerate(data):
        if v != 0:
            continue

        peaks = set()

        stack = [idx]
        while stack:
            idx = stack.pop()
            v = data[idx]
    
            if v == 9:
                peaks.add(idx)
                continue
    
            for y, x in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nidx = (idx[0] + y, idx[1] + x)
    
                if nidx[0] not in range(data.shape[0]) or nidx[1] not in range(data.shape[1]):
                    continue
    
                nv = data[nidx]
                if nv != v + 1:
                    continue
    
                stack.append(nidx)

        sum += len(peaks)

    return sum


def part2(data):
    data = np.array([list(map(int, line[:-1])) for line in data.readlines()])

    sum = 0

    stack = []
    for idx, v in np.ndenumerate(data):
        if v != 0:
            continue

        stack.append(idx)

    while stack:
        idx = stack.pop()
        v = data[idx]

        if v == 9:
            sum += 1
            continue

        for y, x in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nidx = (idx[0] + y, idx[1] + x)

            if nidx[0] not in range(data.shape[0]) or nidx[1] not in range(data.shape[1]):
                continue

            nv = data[nidx]
            if nv != v + 1:
                continue

            stack.append(nidx)

    return sum


def test_part1():
    result = part1(StringIO(dedent('''\
        89010123
        78121874
        87430965
        96549874
        45678903
        32019012
        01329801
        10456732
    ''')))

    assert result == 36


def test_part2():
    result = part2(StringIO(dedent('''\
        89010123
        78121874
        87430965
        96549874
        45678903
        32019012
        01329801
        10456732
    ''')))

    assert result == 81

