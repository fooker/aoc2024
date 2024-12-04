from textwrap import dedent
from io import StringIO




def part1(data):
    data = list(data.readlines())
    w = len(data[0])
    h = len(data)

    def check(x, y, mx, my):
        rx = [x] * 4 if mx == 0 else range(x, x + mx * 4, mx)
        ry = [y] * 4 if my == 0 else range(y, y + my * 4, my)

        if min(rx[0], rx[-1]) < 0:
            return False
        if max(rx[0], rx[-1]) >= w:
            return False

        if min(ry[0], ry[-1]) < 0:
            return False
        if max(ry[0], ry[-1]) >= h:
            return False
        
        return all(data[dy][dx] == l
                   for (dx, dy, l)
                   in zip(rx, ry, 'XMAS'))

    sum = 0
    for x in range(w):
        for y in range(h):
            sum += int(check(x, y,  0, +1))
            sum += int(check(x, y,  0, -1))
            sum += int(check(x, y, +1,  0))
            sum += int(check(x, y, -1,  0))
            sum += int(check(x, y, +1, +1))
            sum += int(check(x, y, +1, -1))
            sum += int(check(x, y, -1, +1))
            sum += int(check(x, y, -1, -1))

    return sum


def part2(data):
    data = list(data.readlines())
    w = len(data[0])
    h = len(data)

    def check(x, y):
        if data[y][x] != 'A':
            return False

        if x not in range(1, w-1):
            return False

        if y not in range(1, h-1):
            return False
        
        a = data[y-1][x-1] == 'M' and data[y+1][x+1] == 'S'
        b = data[y-1][x+1] == 'M' and data[y+1][x-1] == 'S'
        c = data[y+1][x-1] == 'M' and data[y-1][x+1] == 'S'
        d = data[y+1][x+1] == 'M' and data[y-1][x-1] == 'S'

        return (a or d) and (b or c)

    sum = 0
    for x in range(w):
        for y in range(h):
            sum += int(check(x, y))

    return sum



def test_part1():
    result = part1(StringIO(dedent('''\
        MMMSXXMASM
        MSAMXMSMSA
        AMXSXMAAMM
        MSAMASMSMX
        XMASAMXAMM
        XXAMMXXAMA
        SMSMSASXSS
        SAXAMASAAA
        MAMMMXMMMM
        MXMXAXMASX
    ''')))

    assert result == 18


def test_part2():
    result = part2(StringIO(dedent('''\
        MMMSXXMASM
        MSAMXMSMSA
        AMXSXMAAMM
        MSAMASMSMX
        XMASAMXAMM
        XXAMMXXAMA
        SMSMSASXSS
        SAXAMASAAA
        MAMMMXMMMM
        MXMXAXMASX
    ''')))

    assert result == 9

