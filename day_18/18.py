from collections import deque
from typing import NotRequired

def parse(fname, R, C):
    walls = set()
    grid = {}
    wall_list = []
    with open(fname, 'r') as f:
        lines = f.readlines()
        for k, line in enumerate(lines):
            x,y = line.strip().split(',')
            walls.add((int(y), int(x)))
            wall_list.append((int(y), int(x)))
    for i in range(R):
        for j in range(C):
            if (i,j) in walls:
                grid[(i,j)] = '#'
            else:
                grid[(i,j)] = '.'
    return grid, walls, wall_list

def neighbours(node, grid, walls):
    dirs = [(0,1), (1,0), (-1,0), (0,-1)]
    i, j = node
    neighbours = []
    for d in dirs:
        di, dj = d
        n = (i+di, j+dj)
        if n in grid and n not in walls:
            neighbours.append(n)
    return neighbours

def bfs(grid, walls, R, C):
    q = deque([((0,0), 0)]) 
    visited = set()

    while q:
        node, dist = q.popleft()
        if node in visited:
            continue
        visited.add(node)
        if node == (R-1, C-1):
            return dist
        for n in neighbours(node, grid, walls):
            q.append((n, dist+1))

def pr(walls, R, C):
    out = ''
    for i in range(R):
        for j in range(C):
            if (i,j) in walls:
                out += '#'
            else:
                out += '.'
        out += '\n'
    print(out)

if __name__ == "__main__":
    fname = 'input'
    R = 71
    C = 71
    if fname == 'test':
        R = 7
        C = 7
    grid, all_walls, wall_list = parse(fname, R, C)
    walls = all_walls & set(wall_list[:1024])
    # pr(walls, R, C)
    print(f'Part 1: {bfs(grid, walls, R, C)}')

    for k in range(1024, len(all_walls)):
        walls = all_walls & set(wall_list[:k])
        dist = bfs(grid, walls, R, C)
        if dist == None:
            i, j = wall_list[k-1]
            print(f'Part 2: {j},{i}')
            break
