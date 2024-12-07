def deal_increasing(row):
    for a, b in zip(row, row[1:]):
        if b == a:
            return False
        if b < a:
            return False
        if abs(b-a) > 3:
            return False
    return True

def deal_decreasing(row):
    for a, b in zip(row, row[1:]):
        if b == a:
            return False
        if b > a:
            return False
        if abs(b-a) > 3:
            return False
    return True

def process(row):
    a, b = row[0], row[1]
    if a == b:
        return False
    if a < b:
        return deal_increasing(row)
    if a > b:
        return deal_decreasing(row)

with open('input.txt') as f:
    lines = f.readlines()
    count = 0
    count2 = 0
    for line in lines:
        line = [int(n) for n in line.strip().split(' ')]
        if process(line):
            count += 1

        # For part 2
        for i in range(len(line)):
            new_row = line[:i] + line[i+1:]
            if process(new_row):
                count2 += 1
                break

    print(f'Part 1: {count}')
    print(f'Part 2: {count2}')
