def test(report):
    if all(report[i] < report[i+1] for i in range(len(report)-1)) or all(report[i] > report[i+1] for i in range(len(report)-1)):
        if all(abs(report[i] - report[i+1]) <= 3 for i in range(len(report)-1)):
            return True
    return False

safe = 0

with open('day2.txt', 'r') as f:
    reports = [list(map(int, line.strip().split())) for line in f if line.strip()]

for r in reports:
    if test(r) or any(test(r[:i] + r[i+1:]) for i in range(len(r))):
        safe += 1


print(safe)