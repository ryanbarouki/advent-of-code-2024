from collections import deque 

def parse(fname):
    grid = {}
    start = 0
    R = 0
    C = 0
    with open(fname, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        R = len(lines)
        C = len(lines[0])
        for i, l in enumerate(lines):
            for j, c in enumerate(l):
                grid[i+j*1j] = c
                if c == 'S':
                    start = i+j*1j
                    grid[start] = '.'
    return grid, start, R, C

def pr(grid, R, C):
    out = ''
    for i in range(R):
        for j in range(C):
            out += grid[i+j*1j]
        out += '\n'
    print(out)

def neighbours(node, grid):
    dirs = [1, -1, -1j, 1j]
    for d in dirs:
        p = node+d
        if p not in grid:
            continue
        if grid[p] != '#':
            yield p

def bfs(grid, start):
    q = deque([(start, 0)])
    visited = set()
    path = []
    while q:
        node, dist = q.popleft()
        if grid[node] == 'E':
            path.append(node)
            return dist, path
        if node in visited:
            continue
        path.append(node)
        visited.add(node)
        for n in neighbours(node, grid):
            q.append((n, dist+1))

def get_ball(C, R, grid):
    ball = set()
    for p in grid:
        if manhat_dist(C, p) <= R:
            ball.add(p)
    return ball

def manhat_dist(p, q):
    return int(abs(p.real-q.real) + abs(p.imag-q.imag))

def solve(grid, R, full_dist, path, pos_map):
    count = 0
    path_set = set(path)
    for c in path:
        ball = get_ball(c, R, grid)
        for p in path_set & ball:
            if pos_map[p] > pos_map[c]:
                dist = full_dist - pos_map[p] + pos_map[c] + manhat_dist(c,p)
                if full_dist - dist >= 100:
                    count += 1
    return count

if __name__ == "__main__":
    grid, start, R, C = parse('input')
    full_dist, path = bfs(grid, start)

    pos_map = {p:i for i, p in enumerate(path)}
    print(f"Part 1: {solve(grid, 2, full_dist, path, pos_map)}")
    print(f"Part 2: {solve(grid, 20, full_dist, path, pos_map)}")


