import itertools

def initialize_blocks():
    with open("day9.txt") as f:
        data = f.read()
    
    blocks = []
    data_locs = []
    current = 0

    for i, n in enumerate(data):
        if i % 2 == 0:
            blocks.extend(itertools.repeat(current, int(n)))
            data_locs.extend(range(len(blocks) - int(n), len(blocks)))
            current += 1
        else:
            blocks.extend(itertools.repeat(-1, int(n)))


    return blocks, data_locs

def part1(blocks: list[int], data_locs: list[int]) -> int:
    replace_position = len(data_locs) - 1
    blocks_length = len(blocks)

    for i in range(0,  blocks_length):
        if blocks[i] == -1:
            blocks[i] = blocks[data_locs[replace_position]]
            blocks[data_locs[replace_position]] = -1
            replace_position -= 1
        if data_locs[replace_position] <= i:
            break
    
    checksum = 0

    for i in range(0, blocks_length):
        if blocks[i] == -1:
            break
        checksum += i * blocks[i]
    
    return checksum


blocks, data_locs = initialize_blocks()
print(part1(blocks, data_locs))