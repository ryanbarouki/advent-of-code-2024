from collections import defaultdict, deque

def parse(fname):
    grid = {}
    wide_grid = ''
    boxes = set()
    robot = 0
    walls = set()
    with open(fname, 'r') as f:
        G, moves = f.read().strip().split('\n\n')
    for i, line in enumerate(G.split('\n')):
        for j, c in enumerate(line):
            p = i + j*1j
            grid[p] = c
            if c == 'O':
                boxes.add(p)
                wide_grid += '[]'
            elif c == '@':
                robot = p
                wide_grid += '@.'
            elif c == '#':
                walls.add(p)
                wide_grid += '##'
            else:
                wide_grid += '..'
        wide_grid += '\n'
    moves = ''.join([l.strip() for l in moves])
    return grid, wide_grid, moves, robot

def part1(grid, moves, robot):
    dirs = {'v': 1, '>':1j, '<': -1j, '^':-1}
    p = robot
    for m in moves:
        dir = dirs[m]
        i = 1
        move = True
        while True:
            p2 = p+i*dir
            if p2 not in grid:
                move = False
                break
            if grid[p2] == '#':
                move = False
                break
            if grid[p2] == '.':
                break
            if grid[p2] == 'O':
                i += 1
                continue
        if not move:
            continue
        grid[p] = '.'
        grid[p+i*dir] = 'O'
        grid[p+dir] = '@'
        p = p + dir
    return grid

def checksum_p1(grid):
    total = 0
    for p in grid:
        if grid[p] == 'O':
            total += 100*p.real + p.imag
    return int(total)

def make_dict_grid(grid_str):
    grid = {}
    itop = {}
    ptoi = {}
    box_id = 0
    start = 0
    for i, l in enumerate(grid_str.strip().split('\n')):
        for j, c in enumerate(l):
            grid[i+j*1j] = c
            if c == '@':
                start = i+j*1j
            if c == '[':
                p1 = i + j*1j
                p2 = i + (j+1)*1j
                itop[box_id] = [p1, p2]
                ptoi[p1] = box_id
                ptoi[p2] = box_id
                box_id += 1
    return grid, itop, ptoi, start

def get_boxes_to_move(p, dir, grid, ptoi, itop):
    boxes = set([ptoi[p]])
    if dir in [1j, -1j]:
        while p in ptoi:
            boxes.add(ptoi[p])
            p += dir
        if grid[p] == '#':
            return set()
        elif grid[p] == '.':
            return boxes
    else:
        p1, p2 = itop[ptoi[p]]
        q = deque([(p1,p2)])
        while q:
            p1, p2 = q.popleft()
            if grid[p1+dir] == '#' or grid[p2+dir] == '#':
                return set()
            if p1+dir in ptoi:
                boxes.add(ptoi[p1+dir])
                q.append(itop[ptoi[p1+dir]])
            if p2+dir in ptoi:
                boxes.add(ptoi[p2+dir])
                q.append(itop[ptoi[p2+dir]])
        return boxes

def update_box_pos(boxes, itop, dir):
    ptoi = {}
    for id in boxes:
        p1, p2 = itop[id]
        itop[id] = [p1+dir, p2+dir]
    for id, (p1, p2) in itop.items():
        ptoi[p1] = id
        ptoi[p2] = id
    return itop, ptoi

def update_grid(grid, itop):
    new_grid = {}
    for p, c in grid.items():
        if c in '.#':
            new_grid[p] = c
        else:
            new_grid[p] = '.'
    for id, (p1, p2) in itop.items():
        if p1.imag < p2.imag:
            new_grid[p1] = '['
            new_grid[p2] = ']'
        else: 
            new_grid[p2] = '['
            new_grid[p1] = ']'
    return new_grid

def pr(grid, R, C):
    out = ''
    for i in range(R):
        for j in range(C):
            out += grid[i+j*1j]
        out += '\n'
    print(out)


def part2(grid, moves, itop, ptoi, robot):
    dirs = {'v': 1, '>': 1j, '<': -1j, '^': -1}
    p = robot
    for m in moves:
        pr(grid, R, C)
        dir = dirs[m]
        boxes_to_move = set()
        p2 = p+dir
        if p2 not in grid:
            continue
        elif grid[p2] == '#':
            continue
        elif grid[p2] == '.':
            grid[p2] = '@'
            grid[p] = '.'
            p = p2
            continue
        elif p2 in ptoi:
            boxes_to_move = get_boxes_to_move(p2, dir, grid, ptoi, itop)
        if not boxes_to_move:
            continue
        itop, ptoi = update_box_pos(boxes_to_move, itop, dir)
        grid = update_grid(grid, itop)
        grid[p2] = '@'
        p = p2
    return itop

def checksum_p2(itop):
    total = 0
    for id, (p1, p2) in itop.items():
        if p1.imag < p2.imag:
            total += 100*p1.real + p1.imag
        else:
            total += 100*p2.real + p2.imag
    return int(total)

R = 0
C = 0
if __name__ == "__main__":
    grid, wide_grid_str, moves, robot = parse('input')
    grid = part1(grid, moves, robot)
    # print(wide_grid_str) 
    R = len(wide_grid_str.strip().split('\n'))
    C = len(wide_grid_str.split('\n')[0].strip())
    wide_grid, itop, ptoi, robot = make_dict_grid(wide_grid_str)
    itop = part2(wide_grid, moves, itop, ptoi, robot)
    print(f'Part 1: {checksum_p1(grid)}')
    print(f'Part 2: {checksum_p2(itop)}')


