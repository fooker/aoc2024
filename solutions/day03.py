from textwrap import dedent
from io import StringIO

import re


def part1(data):
    return sum(int(a) * int(b) for a, b in re.findall(r'''mul\((\d{1,3}),(\d{1,3})\)''', data.read()))


def part2(data):
    steps = re.finditer(r'''do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\)''', data.read())
    
    en = True
    sum = 0
    for step in steps:
        if step.group() == 'do()':
            en = True
        elif step.group() == 'don\'t()':
            en = False
        elif en:
            sum += int(step.group(1)) * int(step.group(2))

    return sum


def test_part1():
    result = part1(StringIO('''xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'''))

    assert result == 161


def test_part2():
    result = part2(StringIO('''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''))

    assert result == 48

