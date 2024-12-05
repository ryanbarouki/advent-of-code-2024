WORD = 'XMAS'
WORD2 = 'MAS'
DIRS = [(1,0), (0,1), (1,1), (-1,-1), (-1, 0), (0, -1), (1, -1), (-1,1)]
DIRS2 = [(1,1), (-1,-1), (1, -1), (-1,1)]

def process_dir(i, j, dir, grid, word):
    di, dj = dir
    points = [(i,j)]
    for k in range(len(word)-1):
        next = (i+(k+1)*di, j+(k+1)*dj)
        if next in grid.keys() and grid[next] == word[k+1]:
            points.append(next) 
            continue
        else:
            return 0, points
    return 1, points


def part1(grid, nrows, ncols):
    count = 0
    for i in range(nrows):
        for j in range(ncols):
            if grid[(i,j)] == 'X':
                for dir in DIRS:
                    c, _ = process_dir(i, j, dir, grid, WORD)
                    count += c
    print(count)
                        

def part2(grid, nrows, ncols):
    count = 0
    seen = []
    for i in range(nrows):
        for j in range(ncols):
            if grid[(i,j)] == 'M':
                for dir in DIRS2:
                    c, points = process_dir(i, j, dir, grid, WORD2)
                    if c == 1:
                        M,A,S = points
                        ai, aj = A
                        mi, mj = M
                        di, dj = ai-mi, aj-mj
                        corner1 = (mi + 2*di, mj)
                        corner2 = (mi, mj+2*dj)
                        key = set((M,A,S, corner1, corner2))
                        if (grid[corner1] == 'M' and grid[corner2] == 'S') or (grid[corner1] == 'S' and grid[corner2] == 'M'):
                            if key not in seen:
                                count += 1
                                seen.append(key)
    print(count)




with open('input') as f:
    grid = {}
    lines = f.readlines()
    nrows = len(lines)
    ncols = len(lines[0])
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            grid[(i,j)] = c
    
    part1(grid, nrows, ncols)
    part2(grid, nrows, ncols)
