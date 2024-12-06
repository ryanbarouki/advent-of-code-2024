def parse(fname):
    grid = {}
    start = ()
    nrow = 0
    ncol = 0
    with open(fname) as f:
        lines = f.readlines()
        nrow = len(lines)
        ncol = len(lines[0].strip())
        for i, line in enumerate(lines):
            line = line.strip()
            for j, c in enumerate(line):
                if c not in ['#', '.']:
                    start = (i,j)
                    grid[(i,j)] = '.'
                    continue
                grid[(i,j)] = c
    return start, grid, nrow, ncol

def part1(start, grid):
    RIGHT = {(-1, 0): (0, 1), (1, 0): (0, -1), (0, 1): (1, 0), (0, -1): (-1, 0)}
    start_dir = (-1, 0)
    dir = start_dir
    visited = set([start])
    states = set([(start, start_dir)])
    pos = start
    while True:
        di, dj = dir
        i, j = pos
        pos = (i+di, j+dj)
        if pos not in grid:
            return visited, 'left'
        if grid[pos] == '#':
            #turn right
            dir = RIGHT[dir]
            pos = (i, j)
        if (pos, dir) in states:
            return visited, 'cycle'
        visited.add(pos)
        states.add((pos, dir))

def part2(start, grid):
    count = 0
    locs = grid.keys()
    for i, j in locs:
        if (i,j) == start:
            continue
        if grid[(i,j)] == '.':
            grid[(i,j)] = '#'
            _, kind = part1(start, grid)
            if kind == 'cycle':
                count += 1
            grid[(i,j)] = '.'
    return count


def pp(nrow, ncol, visited, grid):
    out = ''
    for i in range(nrow):
        for j in range(ncol):
            if (i,j) in visited:
                out += 'o'
            elif grid[(i,j)] == '#':
                out += '#'
            else:
                out += '.'
        out += '\n'
    print(out)


start, grid, nrow, ncol = parse('input')
visited, _ = part1(start, grid)
pp(nrow, ncol, visited, grid)
print(f'Part 1: {len(visited)}')
print(f'Part 2: {part2(start, grid)}')
