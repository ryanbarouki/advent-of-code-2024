import re

with open('input', 'r') as f:
    total = 0
    total2 = 0
    enabled = True
    for line in f.readlines():
        all = re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", line)
        for match in all:
            if match == 'do()':
                enabled = True
                continue
            elif match == "don't()":
                enabled = False
            else:
                num1, num2 = re.findall(r'\d+', match)
                num1, num2 = int(num1), int(num2)
                total += num1*num2
                if enabled:
                    total2 += num1*num2

    print(f'Part 1: {total}')
    print(f'Part 2: {total2}')
