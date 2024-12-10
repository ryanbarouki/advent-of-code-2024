from collections import deque
import matplotlib.pyplot as plt

def parse(fname):
    with open(fname) as f:
        grid = {}
        image = []
        lines = f.readlines()
        for i, line in enumerate(lines):
            line = line.strip()
            image.append([int(c) for c in line])
            for j, c in enumerate(line):
                grid[(i,j)] = int(c)
    return grid, image


def get_neighbours(grid, node):
    dirs = [(0,1), (1,0), (-1, 0), (0, -1)]
    i,j = node
    neighbours = set()
    for dir in dirs:
        di, dj = dir
        if (i+di, j+dj) not in grid:
            continue
        if grid[(i+di, j+dj)] == grid[node] + 1:
            neighbours.add((i+di, j+dj))
    return neighbours


def bfs(grid, start, part2):
    stack = deque([start])
    visited = set([start])
    count_paths = 0
    while len(stack) > 0:
        node = stack.popleft()
        if grid[node] == 9:
            count_paths += 1
        for n in get_neighbours(grid, node):
            if n in visited:
                continue
            stack.append(n)
            if not part2:
                visited.add(n)
    return count_paths


def find_paths(grid, part2=False):
    total = 0
    for node, height in grid.items():
        if height == 0:
            total += bfs(grid, node, part2)
    return total


grid, image = parse('input')
print(f'Part 1: {find_paths(grid)}')
print(f'Part 2: {find_paths(grid, part2=True)}')

# For funsies
plt.imshow(image)
plt.show()
