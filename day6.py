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
        
        if check_bounds(next_x, next_y) and map[next_y][next_x] != '#':
            x, y = next_x, next_y
        elif not check_bounds(next_x, next_y):
            break
        else:
            orientation = (orientation + 1) % 4

    print(count_tiles())

with open("day6.txt") as f:
    map = [list(line.strip()) for line in f if line.strip()]

UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)
ORIENTATIONS = [UP, RIGHT, DOWN, LEFT]

start_x, start_y = find_start()
part1()