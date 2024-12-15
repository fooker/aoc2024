from textwrap import dedent
from io import StringIO
from dataclasses import dataclass
from functools import reduce

import operator
import re

import numpy as np


@dataclass
class Robot:
    p: (int, int)
    v: (int, int)

    @staticmethod
    def parse(line):
        m = re.match(r'^p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)$', line[:-1])
        return Robot(p=(int(m[1]), int(m[2])),
                     v=(int(m[3]), int(m[4])))

    def pos(self, steps, w, h):
        return ((self.p[0] + steps * self.v[0]) % w,
                (self.p[1] + steps * self.v[1]) % h)


def part1(data, w=101, h=103):
    cx = w // 2
    cy = h // 2

    quadrants = {'NW': list(),
                 'NE': list(),
                 'SW': list(),
                 'SE': list()}

    robots = map(Robot.parse, data.readlines())
    for robot in robots:
        pos = robot.pos(100, w, h)
        
        if pos[0] < cx:
            qx = 'W'
        elif pos[0] > cx:
            qx = 'E'
        else:
            continue

        if pos[1] < cy:
            qy = 'N'
        elif pos[1] > cy:
            qy = 'S'
        else:
            continue

        quadrants[qy + qx].append(pos)
    
    return reduce(operator.mul, map(len, quadrants.values()), 1)


def part2(data, w=101, h=103):
    robots = list(map(Robot.parse, data.readlines()))

    def show(steps):
        p = {robot.pos(steps, w, h) for robot in robots}

        for y in range(h):
            print(''.join('#' if (x, y) in p else '.' for x in range(w)))


    def entropy(steps):
        grid = np.zeros((w, h), dtype=int)
        for pos in (robot.pos(steps, w, h) for robot in robots):
            grid[pos] += 1

        marg = np.histogramdd(np.ravel(grid), bins = 256)[0] / grid.size
        marg = list(filter(lambda p: p > 0, np.ravel(marg)))
        entropy = -np.sum(np.multiply(marg, np.log2(marg)))

        return entropy

    lowest = 9999999.0

    for steps in range(10000000):
        e = entropy(steps)

        if e < lowest:
            print(steps)
            show(steps)

            lowest = e

    return 


def test_part1():
    result = part1(StringIO(dedent('''\
        p=0,4 v=3,-3
        p=6,3 v=-1,-3
        p=10,3 v=-1,2
        p=2,0 v=2,-1
        p=0,0 v=1,3
        p=3,0 v=-2,-2
        p=7,6 v=-1,-3
        p=3,0 v=-1,-2
        p=9,3 v=2,3
        p=7,3 v=-1,2
        p=2,4 v=2,-3
        p=9,5 v=-3,-3
    ''')), w=11, h=7)

    assert result == 12

