from textwrap import dedent
from io import StringIO
from dataclasses import dataclass

import re
import sympy


@dataclass
class Machine:
    btn_a: (int, int)
    btn_b: (int, int)
    prize: (int, int)


def solve(data, offset):
    data = iter(data.readlines())

    machines = []
    while True:
        btn_a = re.match(r'Button A: X\+(\d+), Y\+(\d+)', next(data))
        btn_b = re.match(r'Button B: X\+(\d+), Y\+(\d+)', next(data))
        prize = re.match(r'Prize: X=(\d+), Y=(\d+)', next(data))

        machines.append(Machine(
            btn_a = (int(btn_a[1]), int(btn_a[2])),
            btn_b = (int(btn_b[1]), int(btn_b[2])),
            prize = (int(prize[1]) + offset, int(prize[2]) + offset),
        ))

        try:
            next(data)
        except StopIteration:
            break

    tokens = 0
    for m in machines:

        a, b = sympy.symbols("a, b", integer=True)
        
        ax, bx, px = m.btn_a[0], m.btn_b[0], m.prize[0]
        ay, by, py = m.btn_a[1], m.btn_b[1], m.prize[1]
        
        equations = [
            sympy.Eq(a * ax + b * bx, px), 
            sympy.Eq(a * ay + b * by, py)
        ]

        try:
            solutions = sympy.solve(equations, (a, b), dict=True)
        except sympy.SympifyError:
            continue

        if not solutions:
            continue

        tokens += min(s[a] * 3 + s[b] for s in solutions)
               
    return tokens


def part1(data):
    return solve(data, 0)


def part2(data):
    return solve(data, 10000000000000)



def test_part1():
    result = part1(StringIO(dedent('''\
        Button A: X+94, Y+34
        Button B: X+22, Y+67
        Prize: X=8400, Y=5400
        
        Button A: X+26, Y+66
        Button B: X+67, Y+21
        Prize: X=12748, Y=12176
        
        Button A: X+17, Y+86
        Button B: X+84, Y+37
        Prize: X=7870, Y=6450
        
        Button A: X+69, Y+23
        Button B: X+27, Y+71
        Prize: X=18641, Y=10279
    ''')))

    assert result == 480

