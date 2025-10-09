left = []
right = []
diff = 0

with open('day1.txt', 'r') as f:
    while line := f.readline().strip():
        parts = line.split()
        left.append(int(parts[0]))
        right.append(int(parts[1]))

left.sort()
right.sort()

for l, r in zip(left, right):
    diff += abs(l - r)

print(diff)