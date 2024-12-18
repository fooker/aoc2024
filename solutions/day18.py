from textwrap import dedent
from io import StringIO

import networkx
import bisect


def part1(data, w=70, h=70, l=1024):
    data = (tuple(map(int, line.split(','))) for line in data.readlines()[:l])

    g = networkx.grid_2d_graph(w + 1, h + 1)
    for x, y in set(data):
        g.remove_node((x, y))
    
    p = networkx.astar_path(g, (0, 0), (w, h))
    print(p)

    return len(p) - 1


def part2(data, w=70, h=70, l=1024):
    data = [tuple(map(int, line.split(','))) for line in data.readlines()]

    for i in range(l, len(data)):
        g = networkx.grid_2d_graph(w + 1, h + 1)
        for x, y in set(data[:i]):
            g.remove_node((x, y))
        
        try:
            networkx.astar_path(g, (0, 0), (w, h))
        except networkx.exception.NetworkXNoPath:
            return data[i-1]

    return 



def test_part1():
    result = part1(StringIO(dedent('''\
        5,4
        4,2
        4,5
        3,0
        2,1
        6,3
        2,4
        1,5
        0,6
        3,3
        2,6
        5,1
        1,2
        5,5
        2,5
        6,5
        1,4
        0,4
        6,4
        1,1
        6,1
        1,0
        0,5
        1,6
        2,0
    ''')), w=6, h=6, l=12)

    assert result == 22


def test_part2():
    result = part2(StringIO(dedent('''\
        5,4
        4,2
        4,5
        3,0
        2,1
        6,3
        2,4
        1,5
        0,6
        3,3
        2,6
        5,1
        1,2
        5,5
        2,5
        6,5
        1,4
        0,4
        6,4
        1,1
        6,1
        1,0
        0,5
        1,6
        2,0
    ''')), w=6, h=6, l=12)

    assert result == (6, 1)

