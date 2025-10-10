import re

def next_function(next_f, remaining_program):
    next_index = remaining_program.find(next_f)

    if next_index != -1:
        return next_index + len(next_f)
    return -1

with open('day3.txt', 'r') as f:
    program = f.read()

next_f = "don't()"
enabled = True
enabled_program = ""

while (next_index := next_function(next_f, program)) > -1:
    if enabled:
        enabled_program += program[:next_index]
        next_f = "do()"
        enabled = False
    else:
        next_f = "don't()"
        enabled = True

    program = program[next_index:]

if enabled:
    enabled_program += program

matches = re.findall(r"mul\((\d+),(\d+)\)", enabled_program)
total = sum(int(a) * int(b) for a, b in matches)

print(total)