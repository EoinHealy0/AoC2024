import re
import math

def concat_numbers(x: int, y: int):
    return x * 10 ** (int(math.log10(y)) + 1) + y

def validate_calculation(total: int, operands: list, valid_operators: list):
    current_results = {operands[0]}
    
    for remaining in operands[1:]:
        new_results = set()

        for result in current_results:
            for operator in valid_operators:
                if operator == '+':
                    new_res = result + remaining
                elif operator == '*':
                    new_res = result * remaining
                elif operator == '|':
                    new_res = concat_numbers(result, remaining)
                    
                if new_res <= total:
                    new_results.add(new_res)
            
        if not new_results:
            return False
        
        current_results = new_results
    return total in current_results

def part1(calibrations):
    correct_total = 0

    for equation in calibrations:
        if validate_calculation(equation[0], equation[1:], ['+', '*']):
            correct_total += equation[0]

    print(correct_total)

def part2(calibrations):
    correct_total = 0
    
    for equation in calibrations:
        if validate_calculation(equation[0], equation[1:], ['+', '*', '|']):
            correct_total += equation[0]

    print(correct_total)

with open("day7.txt") as f:
    CALIBRATIONS = [list(map(int, re.findall(r"\d+", line))) for line in f]

part1(CALIBRATIONS)
part2(CALIBRATIONS)