def pages_after(current, remaining_pages):
    valid_pages = after.get(current, [])

    for remaining in remaining_pages:
        if remaining not in valid_pages:
            return False
    return True

def pages_before(current, previous_pages):
    valid_pages = before.get(current, [])

    for previous in previous_pages:
        if previous not in valid_pages:
            return False
    return True

before = {}
after = {}
pages = []
rules = True

with open('day5.txt', 'r') as f:
    for line in f:
        line = line.strip()

        if not line:
            rules = False
            continue

        if rules:
            parts = line.split('|')
            prefix, suffix = parts

            if prefix not in after:
                after[prefix] = []

            after[prefix].append(suffix)

            if suffix not in before:
                before[suffix] = []
                
            before[suffix].append(prefix)
        else:
            pages.append(line.split(','))

page_number_total = 0

for group in pages:
    wrong_order = set()
    i = 0
    
    while i < len(group):
        current = group[i]
        previous = group[:i]

        if not(pages_before(current, previous)):
            group.insert(i - 1, group.pop(i))
            wrong_order.add(current)
            i -= 1
        else:
            i += 1
               
    if wrong_order:
        print(f"Wrong order group: {group}")
        page_number_total += int(group[int(len(group)/2)])

print(page_number_total)