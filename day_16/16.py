import heapq

def parse(fname):
    grid = {}
    start = 0
    end = 0
    with open(fname, 'r') as f:
        D = f.read().strip().split('\n')
    R = len(D)
    C = len(D[0])
    for i, l in enumerate(D):
        for j, c in enumerate(l):
            p = (i,j)
            grid[p] = c
            if c == 'S':
                start = p
                grid[p] = '.'
            if c == 'E':
                end = p
    return grid, start, end, R, C

def get_neighbours(grid, node):
    i,j = node
    for d in [(1,0),(0,1),(0,-1),(-1,0)]:
        di, dj = d
        p = (i+di, j+dj)
        if grid[p] != '#':
            yield p, d


def dijkstra(start, grid):
    pq = [(0, (0,1), start, [(start, (0,1))])]
    visited = set()
    while pq:
        dist, dir, node, path = heapq.heappop(pq)
        if (node, dir) in visited:
            continue
        visited.add((node, dir))
        if grid[node] == 'E':
            return dist, path
        for n, ndir in get_neighbours(grid, node):
            ndist = dist + 1
            if ndir != dir:
                ndist += 1000
            heapq.heappush(pq, (ndist, ndir, n, path + [(n,ndir)]))

def dijkstra_all_shortest_paths(start, grid):
    pq = [(0, (0,1), start, [(start, (0,1))])]
    visited_dist = {}

    best_dist = None
    end_paths = []

    while pq:
        dist, dir, node, path = heapq.heappop(pq)

        if (node, dir) in visited_dist:
            if dist > visited_dist[(node, dir)]:
                continue
        else:
            visited_dist[(node, dir)] = dist

        if grid[node] == 'E':
            if best_dist is None or dist == best_dist:
                best_dist = dist
                end_paths.append(path)
            continue

        for n, ndir in get_neighbours(grid, node):
            ndist = dist + 1
            if ndir != dir:
                ndist += 1000

            heapq.heappush(pq, (ndist, ndir, n, path + [(n, ndir)]))

    return best_dist, end_paths

def pr(grid, path, R, C):
    pathset = set([p for p, dir in path])
    path_to_dir = {p:d for p, d in path}
    dirs = {(1,0):'v', (0,1):'>', (-1,0): '^', (0,-1): '<'}
    out = ''
    for i in range(R):
        for j in range(C):
            if (i,j) in pathset:
                out += dirs[path_to_dir[(i,j)]]
            else:
                out += grid[(i,j)]
        out += '\n'
    print(out)


if __name__ == "__main__":
    grid, start, end, R, C = parse('input')
    dist, path = dijkstra(start, grid)
    print(f'Part 1: {dist}')
    dist, paths = dijkstra_all_shortest_paths(start, grid)
    
    all_points = set()
    for path in paths:
        for p, d in path:
            all_points.add(p)
    print(f'Part 2: {len(all_points)}')
    # print(paths)
    # print(len(paths[0]))
    # pr(grid, path, R, C)
    # print(dist)
