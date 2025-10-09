left = []
right_counts = {}
total = 0

with open('day1.txt', 'r') as f:
    while line := f.readline().strip():
        parts = line.split()
        left.append(int(parts[0]))
        right = int(parts[1])
        right_counts[right] = right_counts.get(right, 0) + 1

for l in left:
    total += right_counts.get(l, 0) * l

print(total)