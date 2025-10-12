from itertools import groupby
def load_data():
    len_x, len_y = 0, 0
    with open('day8.txt', 'r') as f:
        coords: dict[str, list] = {}

        for y, line in enumerate(f):
            line = line.strip()
            len_y += 1
            len_x = len(line)

            for x, antenna in enumerate(line):
                if antenna != '.':
                    if coords.get(antenna):
                        coords[antenna].append((x, y))
                    else:
                        coords[antenna] = [(x, y)]

    return coords, len_x, len_y

def check_bounds(x, y, bound_x, bound_y):
    return 0 <= x < bound_x and 0 <= y < bound_y

def get_distance(a, b):
    return ((a[0] - b[0]), (a[1] - b[1]))

def part1(coords, bound_x, bound_y):
    nefs = set()

    for points in coords.values():
        for i in range(len(points)):
            a = points[i]

            for j in range(i + 1, len(points)):
                b = points[j]
                d = get_distance(a, b)
                nef_point = (a[0] + d[0], a[1] + d[1])

                if check_bounds(nef_point[0], nef_point[1], bound_x, bound_y):
                    nefs.add(nef_point)

                nef_point = (b[0] - d[0], b[1] - d[1])

                if check_bounds(nef_point[0], nef_point[1], bound_x, bound_y):
                    nefs.add(nef_point)
    
    print(len(nefs))

def max_steps(point, d, bound_x, bound_y):
    if(d[0] < 0):
        x_mult = int(point[0] // (-d[0]))
    elif(d[0] > 0):
        x_mult = int((bound_x - point[0] - 1) // d[0])
    else:
        x_mult = float('inf')

    if(d[1] < 0):
        y_mult = int(point[1] // (-d[1]))
    elif(d[1] > 0):
        y_mult = int((bound_y - point[1] - 1) // d[1])
    else:
        y_mult = float('inf')

    return int(min(x_mult, y_mult))

def part2(coords, bound_x, bound_y):
    nefs = set()

    for points in coords.values():
        for i in range(len(points)):
            a = points[i]

            if len(points) != 1:
                nefs.add(a)

            for j in range(i + 1, len(points)):
                b = points[j]
                d = get_distance(a, b)
                
                for mult in range(1, max_steps(a, d, bound_x, bound_y) + 1):
                    nef_point = (a[0] + mult * d[0], a[1] + mult * d[1])
                    nefs.add(nef_point)

                for mult in range(1, max_steps(b, (-d[0], -d[1]), bound_x, bound_y) + 1):
                    nef_point = (b[0] - mult * d[0], b[1] - mult * d[1])
                    nefs.add(nef_point)
    print(len(nefs))

part1(*load_data())
part2(*load_data())
