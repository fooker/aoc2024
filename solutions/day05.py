from textwrap import dedent
from io import StringIO
from itertools import takewhile, product

import functools


def check(rules, pages):
    return all(n == m or (n < m and (x, y) in rules) or (n > m and (y, x) in rules)
                for (n, x), (m, y)
                in product(enumerate(pages), enumerate(pages)))


def part1(data):
    rules = set()
    for line in takewhile(lambda l: l != "\n", data):
        b, a = map(int, line.split('|'))
        rules.add((b, a))
    
    sum = 0
    for line in data:
        pages = list(map(int, line.split(',')))

        if check(rules, pages):
            sum += pages[(len(pages) - 1) // 2]

    return sum


def part2(data):
    rules = set()
    for line in takewhile(lambda l: l != "\n", data):
        b, a = map(int, line.split('|'))
        rules.add((b, a))
    
    def srt(x, y):
        if x == y:
            return 0
        elif (x, y) in rules:
            return -1
        else:
            return +1

    sum = 0
    for line in data:
        pages = list(map(int, line.split(',')))

        if check(rules, pages):
            continue

        pages = sorted(pages, key=functools.cmp_to_key(srt))
        sum += pages[(len(pages) - 1) // 2]

    return sum



def test_part1():
    result = part1(StringIO(dedent('''\
        47|53
        97|13
        97|61
        97|47
        75|29
        61|13
        75|53
        29|13
        97|29
        53|29
        61|53
        97|53
        61|29
        47|13
        75|47
        97|75
        47|61
        75|61
        47|29
        75|13
        53|13
        
        75,47,61,53,29
        97,61,53,29,13
        75,29,13
        75,97,47,61,53
        61,13,29
        97,13,75,29,47
    ''')))

    assert result == 143


def test_part2():
    result = part2(StringIO(dedent('''\
        47|53
        97|13
        97|61
        97|47
        75|29
        61|13
        75|53
        29|13
        97|29
        53|29
        61|53
        97|53
        61|29
        47|13
        75|47
        97|75
        47|61
        75|61
        47|29
        75|13
        53|13
        
        75,47,61,53,29
        97,61,53,29,13
        75,29,13
        75,97,47,61,53
        61,13,29
        97,13,75,29,47
    ''')))

    assert result == 123

