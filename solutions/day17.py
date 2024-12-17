from textwrap import dedent
from io import StringIO


def parse(data):
    a = int(data.readline().split(': ')[1].strip())
    b = int(data.readline().split(': ')[1].strip())
    c = int(data.readline().split(': ')[1].strip())
    _ = data.readline()
    p = list(map(int, data.readline().split(': ')[1].strip().split(',')))

    return a, b, c, p


def eval(a, b, c, p):
    out = list()

    pc = 0

    while pc < len(p):
        i = p[pc + 0]
        o = p[pc + 1]

        match o:
            case 0 | 1 | 2 | 3: m = o
            case 4: m = a
            case 5: m = b
            case 6: m = c

        match i:
            case 0: # ADV
                a = a >> m

            case 1: # BXL
                b = b ^ o

            case 2: # BST
                b = m % 8

            case 3: # JNZ
                if a != 0:
                    pc = o
                    continue
            
            case 4: # BXC
                b = b ^ c

            case 5: # OUT
                out.append(m % 8)

            case 6: # BDV
                b = a >> m
            
            case 7: # CDV
                c = a >> m

        pc += 2

    return out


def part1(data):
    a, b, c, p = parse(data)
    out = eval(a, b, c, p)
    return ','.join(map(str, out))


def part2(data):
    a, b, c, p = parse(data)
    
    def find(a, i):
        for x in range(8):
            ax = (a << 3) + x
            if eval(ax, b, c, p) == p[-i:]:
                if i == len(p):
                    return ax

                if (ret := find(ax, i + 1)) is not None:
                    return ret

        return None

    return find(0, 1)


def test_part1():
    result = part1(StringIO(dedent('''\
        Register A: 729
        Register B: 0
        Register C: 0

        Program: 0,1,5,4,3,0
    ''')))

    assert result == '4,6,3,5,6,3,5,2,1,0'


def test_part2():
    result = part2(StringIO(dedent('''\
        Register A: 2024
        Register B: 0
        Register C: 0

        Program: 0,3,5,4,3,0
    ''')))

    assert result == 117440

