from textwrap import dedent
from io import StringIO

import numpy as np


def gm(guard, move):
    return (guard[0] + move[0], guard[1] + move[1])


moves = {
    'N': ((-1,  0), 'E'),
    'E': (( 0,  1), 'S'),
    'S': (( 1,  0), 'W'),
    'W': (( 0, -1), 'N'),
}

def walk(map, guard, dir):
    steps = set()

    while True:
        map[guard] = dir

        if (guard, dir) in steps:
            # Stuck in a loop
            return None

        steps.add((guard, dir))

        move, rot = moves[dir]
        step = gm(guard, move)

        if step[0] not in range(map.shape[0]) or step[1] not in range(map.shape[1]):
            break

        if map[step] in ('#', 'O'):
            dir = rot
            continue

        guard = step

    return steps


def part1(data):
    map = np.array([list(line[:-1]) for line in data.readlines()])

    guard = None
    for idx, v in np.ndenumerate(map):
        if v == '^':
            guard = idx
            break

    steps = walk(map, guard, 'N')
    
    return len({ step for step, dir in steps })


def part2(data):
    map = np.array([list(line[:-1]) for line in data.readlines()])

    guard = None
    for idx, v in np.ndenumerate(map):
        if v == '^':
            guard = idx
            break

    steps = walk(np.copy(map), guard, 'N')

    # Every step on the normal route is something that could possibly be blocked and has a chance to form a loop
    loops = set()
    for (step, dir) in steps:
        move, rot = moves[dir]

        obstruct = gm(step, move)

        if obstruct[0] not in range(map.shape[0]) or obstruct[1] not in range(map.shape[1]):
            continue

        mapx = np.copy(map)
        mapx[obstruct] = 'O'

        if walk(mapx, guard, 'N') is None:
            loops.add(obstruct)

    return len(loops)



def test_part1():
    result = part1(StringIO(dedent('''\
        ....#.....
        .........#
        ..........
        ..#.......
        .......#..
        ..........
        .#..^.....
        ........#.
        #.........
        ......#...
    ''')))

    assert result == 41


def test_part2():
    result = part2(StringIO(dedent('''\
        ....#.....
        .........#
        ..........
        ..#.......
        .......#..
        ..........
        .#..^.....
        ........#.
        #.........
        ......#...
    ''')))

    assert result == 6

