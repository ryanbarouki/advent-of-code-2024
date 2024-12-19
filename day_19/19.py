from collections import deque

def parse(fname):
    with open(fname, 'r') as f:
        towels, designs = f.read().strip().split('\n\n')
    towels = towels.split(', ')
    designs = designs.split('\n')
    return towels, designs

def get_possible_towels(design, towels, i):
    return [k for k in range(len(design)-1, i-1, -1) if design[i:k+1] in towels]

def can_make_towel(design, towels):
    start = get_possible_towels(design, towels, 0)
    q = deque(start)

    while q:
        i = q.pop()
        if i == len(design)-1:
            return True
        for k in get_possible_towels(design, towels, i+1):
            q.append(k)

    return False

CACHE = {}
def ways(towels, design):
    if design in CACHE:
        return CACHE[design]
    ans = 0
    if len(design) == 0:
        ans = 1
    for t in towels:
        if design.startswith(t):
            ans += ways(towels, design[len(t):])
    CACHE[design] = ans
    return ans

def part1(towels, designs):
    count = 0
    for design in designs:
        count += can_make_towel(design, towels)
    return count

def part2(towels, designs):
    count = 0
    for design in designs:
        count += ways(towels, design)
    return count

if __name__ == "__main__":
    towels, designs = parse('input')
    print(f'Part 1: {part1(set(towels), designs)}')
    print(f'Part 2: {part2(towels, designs)}')
