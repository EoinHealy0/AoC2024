import copy


def find_start():
    start_chars = ['^', '>', 'v', '<']

    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] in start_chars:
                return (j, i)
            
    return (-1, -1)

def check_bounds(x, y):
    return 0 <= x < len(map[0]) and 0 <= y < len(map)

def count_tiles():
    count = 0

    for row in map:
        for tile in row:
            if tile == 'X':
                count += 1

    return count

def part1():
    orientation = 0
    x, y = start_x, start_y

    while check_bounds(x, y):
        map[y][x] = 'X'
        next_x, next_y = x + ORIENTATIONS[orientation][0], y + ORIENTATIONS[orientation][1]
        
        if check_bounds(next_x, next_y): 
            if map[next_y][next_x] != '#':
                x, y = next_x, next_y
            else:
                orientation = (orientation + 1) % 4
        else:
            break

    print(count_tiles())

def part2():
    infinite_placements = 0

    for block_y in range(len(map)):
        for block_x in range(len(map[0])):
            if map[block_y][block_x] == '.':
                current_map = copy.deepcopy(map)
                current_map[block_y][block_x] = '#'

                orientation = 0
                x, y = start_x, start_y
                previous_blocks = []

                while check_bounds(x, y):
                    next_x, next_y = x + ORIENTATIONS[orientation][0], y + ORIENTATIONS[orientation][1]

                    if (x, y, orientation) in previous_blocks:
                        infinite_placements += 1
                        print(f"Block at ({block_x}, {block_y}) causes infinite loop.")
                        break

                    if check_bounds(next_x, next_y): 
                        if current_map[next_y][next_x] != '#':
                            x, y = next_x, next_y
                        else:
                            previous_blocks.append((x, y, orientation))
                            orientation = (orientation + 1) % 4
                    else:
                        break

    print(infinite_placements)

with open("day6.txt") as f:
    map = [list(line.strip()) for line in f if line.strip()]

UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)
ORIENTATIONS = [UP, RIGHT, DOWN, LEFT]

start_x, start_y = find_start()
#part1()
part2()