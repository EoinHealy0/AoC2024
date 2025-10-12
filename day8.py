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

part1(*load_data())
