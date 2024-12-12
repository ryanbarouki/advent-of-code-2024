from collections import deque

def parse(fname):
    grid = {}
    with open(fname, 'r') as f:
        D = f.read().strip().split('\n')
    R = len(D)
    C = len(D[0])
    for i, line in enumerate(D):
        for j, c in enumerate(line):
            grid[i + j*1j] = c
    return grid, R, C

def get_neighbours(node, grid):
    neighbours = []
    dirs = [1, -1, -1j, 1j]
    for dir in dirs:
        if node+dir in grid:
            if grid[node+dir] == grid[node]:
                neighbours.append(node+dir)
    return neighbours

def get_area_and_perimeter(start, grid):
    q = deque([start])
    visited = set([start])
    perimeter = 0
    while len(q) > 0:
        node = q.popleft()
        neighbours = get_neighbours(node, grid)
        perimeter += 4 - len(neighbours)
        for n in neighbours:
            if n in visited:
                continue
            q.append(n)
            visited.add(n)
    return visited, perimeter

def count_corners(area, R, C):
    count = 0
    # 1 0 or 1 1 etc are what corners look like
    # 0 0    1 0
    CORNERS = set([(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(1,1,1,0),(1,1,0,1),(1,0,1,1),(0,1,1,1)])
    # 1 0 and 0 1 are special edge cases that count as 2
    # 0 1     1 0
    SPECIAL_CORNERS = set([(1,0,0,1), (0,1,1,0)])
    for i in range(-1, R):
        for j in range(-1, C):
            p = i + j*1j
            corner_mask = tuple([d+p in area for d in [0, 1j, 1, 1+1j]])
            if corner_mask in CORNERS:
                count += 1
            elif corner_mask in SPECIAL_CORNERS:
                count += 2
    return count

def solve(grid, R, C):
    global_visited = set()
    total = 0
    total2 = 0
    for p in grid:
        if p in global_visited:
            continue
        v, per = get_area_and_perimeter(p, grid)
        global_visited |= v
        sides = count_corners(v, R, C) # corners = sides
        total += len(v)*per
        total2 += len(v)*sides
    return total, total2

grid, R, C = parse('input')
part1, part2 = solve(grid, R, C)

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')

