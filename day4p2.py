def check_direction(x, y, dx, dy):
    if x < 0 or y < 0:
        return False
    if dx == 1 and x + wordlength > len(wordsearch[0]):
        return False
    if dy == 1 and y + wordlength > len(wordsearch):
        return False
    if dx == -1 and (x + 1 - wordlength < 0 or x >= len(wordsearch[0])):
        return False
    if dy == -1 and (y + 1 - wordlength < 0 or y >= len(wordsearch)):
        return False
    
    for i in range(wordlength):
        if wordsearch[y + i * dy][x + i * dx] != word[i]:
            return False
        
    return True

with open('day4.txt', 'r') as f:
    wordsearch = [line.strip() for line in f]

word = "MAS"
wordlength = len(word)
count = 0

for v in range(len(wordsearch)):
    for h in range(len(wordsearch[0])):
        if wordsearch[v][h] == 'A':
            tcount = 0
            tcount += check_direction(h - 1, v - 1,  1, 1) # diag right down
            tcount += check_direction(h + 1, v - 1, -1, 1) # diag left down
            tcount += check_direction(h - 1, v + 1,  1, -1) # diag right up
            tcount += check_direction(h + 1, v + 1, -1, -1) # diag left up
            
            if tcount == 2:
                print(f"Diagonal found at {h},{v}")
                count += 1

print(count)