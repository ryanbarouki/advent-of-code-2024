from collections import defaultdict
from functools import cmp_to_key

def process_page(page, greater_than):
    for i, num in enumerate(page):
        for j in range(i+1, len(page)):
            if page[j] not in greater_than[num]:
                return None
    return page

def part1(pages, greater_than):
    count = 0
    correct_pages = []
    for page in pages:
        processed = process_page(page, greater_than)
        if processed is not None:
            correct_pages.append(processed)
    for p in correct_pages:
        assert len(p) % 2 == 1
        count += p[len(p)//2]
    return count

def part2(pages, greater_than):
    sorted_pages = []
    for p in pages:
        if process_page(p, greater_than) is not None:
            continue

        def cmp(a,b):
            if b in greater_than[a]:
                return -1
            else:
                return 1

        sorted_p = sorted(p, key=cmp_to_key(cmp))
        sorted_pages.append(sorted_p)

    count = 0
    for sp in sorted_pages:
        count += sp[len(sp)//2]
    return count


with open('input') as f:
    lines = f.readlines()
    greater_than = defaultdict(set)
    pages = []
    for line in lines:
        line = line.strip()
        if '|' in line:
            a, b = line.split('|')
            greater_than[int(a)].add(int(b))
        elif ',' in line:
            pages.append([int(num) for num in line.split(',')])

    print(f'Part 1: {part1(pages, greater_than)}')
    print(f'Part 2: {part2(pages, greater_than)}')


