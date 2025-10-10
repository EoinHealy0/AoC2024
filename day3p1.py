import re

with open('day3.txt', 'r') as f:
    program = f.read()

matches = re.findall(r"mul\((\d+),(\d+)\)", program)
total = sum(int(a) * int(b) for a, b in matches)

print(total)