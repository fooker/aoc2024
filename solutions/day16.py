from textwrap import dedent
from io import StringIO
from itertools import chain
from networkx import DiGraph, shortest_path_length, all_shortest_paths

import numpy as np


def va(p, y, x):
    return (p[0] + y, p[1] + x)


def graph(data):
    grid = np.array([list(line) for line in data.readlines()])

    g = DiGraph()
    for idx, v in np.ndenumerate(grid[1:-1, 1:-1]):
        idx = va(idx, 1, 1) # Fix up index to match slice

        if v == '#':
            continue

        if v == 'S':
            g.add_node('S')
            g.add_edge('S', (idx, '>'), weight=0)

        if v == 'E':
            g.add_node('E')
            g.add_edge((idx, '^'), 'E', weight=0)
            g.add_edge((idx, 'v'), 'E', weight=0)
            g.add_edge((idx, '<'), 'E', weight=0)
            g.add_edge((idx, '>'), 'E', weight=0)

        g.add_node((idx, '^'))
        g.add_node((idx, 'v'))
        g.add_node((idx, '<'))
        g.add_node((idx, '>'))

        g.add_edge((idx, '^'), (idx, '>'), weight=1000)
        g.add_edge((idx, '>'), (idx, 'v'), weight=1000)
        g.add_edge((idx, 'v'), (idx, '<'), weight=1000)
        g.add_edge((idx, '<'), (idx, '^'), weight=1000)

        g.add_edge((idx, '^'), (idx, '<'), weight=1000)
        g.add_edge((idx, '<'), (idx, 'v'), weight=1000)
        g.add_edge((idx, 'v'), (idx, '>'), weight=1000)
        g.add_edge((idx, '>'), (idx, '^'), weight=1000)

        if grid[va(idx, -1, 0)] != '#': g.add_edge((idx, '^'), (va(idx, -1, 0), '^'), weight=1)
        if grid[va(idx, +1, 0)] != '#': g.add_edge((idx, 'v'), (va(idx, +1, 0), 'v'), weight=1)
        if grid[va(idx, 0, -1)] != '#': g.add_edge((idx, '<'), (va(idx, 0, -1), '<'), weight=1)
        if grid[va(idx, 0, +1)] != '#': g.add_edge((idx, '>'), (va(idx, 0, +1), '>'), weight=1)

    return g


def part1(data):
    g = graph(data)
    return shortest_path_length(g, 'S', 'E', weight='weight')


def part2(data):
    g = graph(data)
    
    seats = chain.from_iterable(all_shortest_paths(g, 'S', 'E', weight='weight'))
    seats = {seat[0] for seat in seats if seat not in ('S', 'E')}

    return len(seats)



def test_part1_1():
    result = part1(StringIO(dedent('''\
        ###############
        #.......#....E#
        #.#.###.#.###.#
        #.....#.#...#.#
        #.###.#####.#.#
        #.#.#.......#.#
        #.#.#####.###.#
        #...........#.#
        ###.#.#####.#.#
        #...#.....#.#.#
        #.#.#.###.#.#.#
        #.....#...#.#.#
        #.###.#.#.#.#.#
        #S..#.....#...#
        ###############
    ''')))

    assert result == 7036


def test_part1_2():
    result = part1(StringIO(dedent('''\
        #################
        #...#...#...#..E#
        #.#.#.#.#.#.#.#.#
        #.#.#.#...#...#.#
        #.#.#.#.###.#.#.#
        #...#.#.#.....#.#
        #.#.#.#.#.#####.#
        #.#...#.#.#.....#
        #.#.#####.#.###.#
        #.#.#.......#...#
        #.#.###.#####.###
        #.#.#...#.....#.#
        #.#.#.#####.###.#
        #.#.#.........#.#
        #.#.#.#########.#
        #S#.............#
        #################
    ''')))

    assert result == 11048


def test_part2_1():
    result = part2(StringIO(dedent('''\
        ###############
        #.......#....E#
        #.#.###.#.###.#
        #.....#.#...#.#
        #.###.#####.#.#
        #.#.#.......#.#
        #.#.#####.###.#
        #...........#.#
        ###.#.#####.#.#
        #...#.....#.#.#
        #.#.#.###.#.#.#
        #.....#...#.#.#
        #.###.#.#.#.#.#
        #S..#.....#...#
        ###############
    ''')))

    assert result == 45


def test_part2_2():
    result = part2(StringIO(dedent('''\
        #################
        #...#...#...#..E#
        #.#.#.#.#.#.#.#.#
        #.#.#.#...#...#.#
        #.#.#.#.###.#.#.#
        #...#.#.#.....#.#
        #.#.#.#.#.#####.#
        #.#...#.#.#.....#
        #.#.#####.#.###.#
        #.#.#.......#...#
        #.#.###.#####.###
        #.#.#...#.....#.#
        #.#.#.#####.###.#
        #.#.#.........#.#
        #.#.#.#########.#
        #S#.............#
        #################
    ''')))

    assert result == 64
