from textwrap import dedent
from io import StringIO
from itertools import batched
from dataclasses import dataclass


@dataclass
class Block:
    idx: int
    files: list[int]
    space: int


def csum(blocks):
    csum = 0

    idx = 0
    for block in blocks:
        for file in block.files:
            csum += idx * file
            idx += 1
        idx += block.space
    
    return csum

def dbg(blocks):
    print(''.join(
        (''.join(map(str, block.files))) + ('.' * block.space)
        for block in blocks))



def part1(data):
    data = map(int, data.read()[:-1])

    blocks = []
    spaces = []

    for idx, file in enumerate(data):
        try:
            free = next(data)
        except StopIteration:
            free = 0

        blocks.append(Block(
            idx = idx,
            files = [idx] * file,
            space = free
        ))

        if free > 0:
            spaces.append(idx)

    while spaces:
        if not blocks[-1].files:
            # Empty block at end of disk, drop it
            blocks = blocks[0:-1]
            continue

        if spaces[0] >= len(blocks):
            # Space points to end of disk, ignore it
            spaces.pop(0)
            continue

        if not blocks[spaces[0]].space:
            # Space block has no space left, move to next
            spaces.pop(0)
            continue

        file = blocks[-1].files.pop()
        
        blocks[spaces[0]].files.append(file)
        blocks[spaces[0]].space -= 1

    return csum(blocks)


def part2(data):
    data = map(int, data.read()[:-1])

    blocks = []

    for idx, file in enumerate(data):
        try:
            free = next(data)
        except StopIteration:
            free = 0

        blocks.append(Block(
            idx = idx,
            files = [idx] * file,
            space = free
        ))

    i = len(blocks) - 1
    while i > 1:
        # Try to find the first matching free space
        for j in range(i):
            if blocks[j].space >= len(blocks[i].files):
                block = blocks.pop(i)

                # Extend heading block free space
                blocks[i - 1].space += block.space + len(block.files)

                # Move remaining free space from traget block
                block.space = blocks[j].space - len(block.files)
                blocks[j].space = 0

                blocks.insert(j + 1, block)

                break
        else:
            i -= 1

    return csum(blocks)



def test_part1():
    result = part1(StringIO(dedent('''\
        2333133121414131402
    ''')))

    assert result == 1928


def test_part2():
    result = part2(StringIO(dedent('''\
        2333133121414131402
    ''')))

    assert result == 2858

