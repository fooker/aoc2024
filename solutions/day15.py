from textwrap import dedent
from io import StringIO

import numpy as np


def m(p, v):
    return (p[0] + v[0],
            p[1] + v[1])


def r(p):
    return m(p, (0, +1))


def l(p):
    return m(p, (0, -1))


moves = {'^': (-1, 0),
         'v': (+1, 0),
         '<': (0, -1),
         '>': (0, +1)}


def solve(grid, commands):
    for idx, v in np.ndenumerate(grid):
        if v == '@':
            robot = idx
            grid[idx] = '.'
            break

    for cmd in commands:
        v = moves[cmd]
        
        def push(p, t, n):
            if grid[p] == '.':
                return True

            if grid[p] == '#':
                return False

            if grid[p] in ('[', ']'):
                if cmd in ('^', 'v'):
                    if grid[p] == '[': o = r
                    if grid[p] == ']': o = l

                    if push(m(p, v), True, n + 1) and push(m(o(p), v), True, n + 1):
                        if not t:
                            push(m(p, v), False, n + 1)
                            push(m(o(p), v), False, n + 1)
    
                            grid[m(p, v)] = grid[p]
                            grid[p] = '.'
    
                            grid[m(o(p), v)] = grid[o(p)]
                            grid[o(p)] = '.'
                        
                        return True

                if cmd in ('<', '>'):
                    if push(m(p, v), True, n + 1):
                        if not t:
                            push(m(p, v), False, n + 1)

                            grid[m(p, v)] = grid[p]
                            grid[p] = '.'
                    
                        return True

            if grid[p] == 'O':
                if push(m(p, v), True, n + 1):
                    if not t:
                        push(m(p, v), False, n + 1)

                        grid[m(p, v)] = grid[p]
                        grid[p] = '.'
                    
                    return True

            return False

        if push(m(robot, v), False, 0):
            robot = m(robot, v)

    gps = 0
    for idx, v in np.ndenumerate(grid):
        if v not in ('O', '['):
            continue

        gps += idx[0] * 100 + idx[1]

    return gps


def part1(data):
    grid, commands = data.read().split('\n\n')
    grid = np.array([list(line) for line in grid.splitlines()])
    commands = ''.join(commands.splitlines())

    return solve(grid, commands)


def part2(data):
    grid, commands = data.read().split('\n\n')
    grid = np.array([list(line.replace('.', '..').replace('O', '[]').replace('#', '##').replace('@', '@.'))
                     for line
                     in grid.splitlines()])
    commands = ''.join(commands.splitlines())

    return solve(grid, commands)




def test_part1():
    result = part1(StringIO(dedent('''\
        ##########
        #..O..O.O#
        #......O.#
        #.OO..O.O#
        #..O@..O.#
        #O#..O...#
        #O..O..O.#
        #.OO.O.OO#
        #....O...#
        ##########
        
        <vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
        vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
        ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
        <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
        ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
        ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
        >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
        <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
        ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
        v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
    ''')))

    assert result == 10092


def test_part2():
    result = part2(StringIO(dedent('''\
        ##########
        #..O..O.O#
        #......O.#
        #.OO..O.O#
        #..O@..O.#
        #O#..O...#
        #O..O..O.#
        #.OO.O.OO#
        #....O...#
        ##########
        
        <vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
        vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
        ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
        <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
        ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
        ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
        >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
        <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
        ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
        v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
    ''')))

    assert result == 9021


def test_part2_small():
    result = part2(StringIO(dedent('''\
        #######
        #...#.#
        #.....#
        #..OO@#
        #..O..#
        #.....#
        #######
        
        <vv<<^^<<^^
    ''')))

