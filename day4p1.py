def check_direction(x, y, dx, dy):
    if dx == 1 and x + wordlength > len(wordsearch[0]):
        return False
    if dy == 1 and y + wordlength > len(wordsearch):
        return False
    if dx == -1 and x + 1 - wordlength < 0:
        return False
    if dy == -1 and y + 1 - wordlength < 0:
        return False
    
    for i in range(wordlength):
        if wordsearch[y + i * dy][x + i * dx] != word[i]:
            return False
        
    print(f"Found {word} at {x},{y} direction {dx},{dy}")
    return True

with open('day4.txt', 'r') as f:
    wordsearch = [line.strip() for line in f]

word = "XMAS"
wordlength = len(word)
count = 0

for v in range(len(wordsearch)):
    for h in range(len(wordsearch[0])):
        count += check_direction(h, v, 1, 0) # right
        count += check_direction(h, v, 0, 1) # down
        count += check_direction(h, v, -1, 0) # left
        count += check_direction(h, v, 0, -1) # up
        count += check_direction(h, v, 1, 1) # diag right down
        count += check_direction(h, v, 1, -1) # diag right up
        count += check_direction(h, v, -1, -1) # diag left up
        count += check_direction(h, v, -1, 1) # diag left down

print(count)