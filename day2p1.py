safe = 0

with open('day2.txt', 'r') as f:
    reports = [list(map(int, line.strip().split())) for line in f if line.strip()]

for r in reports:
    if all(r[i] < r[i+1] for i in range(len(r)-1)) or all(r[i] > r[i+1] for i in range(len(r)-1)):
        if all(abs(r[i] - r[i+1]) <= 3 for i in range(len(r)-1)):
            safe += 1

print(safe)