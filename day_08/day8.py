from collections import defaultdict

def parse(fname):
    grid = {}
    antenna = defaultdict(list)
    with open(fname) as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            line = line.strip()
            for j, c in enumerate(line):
                pos = i + j*1j
                grid[pos] = c
                if c != '.':
                    antenna[c].append(pos)
    return grid, antenna

def part1(grid, antenna):
    antinodes = set()
    for ant, positions in antenna.items():
        for i, p1 in enumerate(positions):
            for p2 in positions[i+1:]:
                dir = p2 - p1
                antinode1 = p1 + 2*dir
                antinode2 = p1 - dir
                if antinode1 in grid:
                    antinodes.add(antinode1)
                if antinode2 in grid:
                    antinodes.add(antinode2)
    return len(antinodes)

def part2(grid, antenna):
    antinodes = set()
    for ant, positions in antenna.items():
        for i, p1 in enumerate(positions):
            for p2 in positions[i+1:]:
                dir = p2 - p1
                i = 0
                while p1 + i*dir in grid:
                    antinodes.add(p1 + i*dir)
                    i += 1
                i = 0
                while p1 - i*dir in grid:
                    antinodes.add(p1 - i*dir)
                    i += 1
    return len(antinodes)

grid, antenna = parse('input')
print(f'Part 1: {part1(grid, antenna)}')
print(f'Part 2: {part2(grid, antenna)}')
