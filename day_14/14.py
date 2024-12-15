import re
import time
from collections import deque
import sys

def parse(fname):
    robots = []
    with open(fname, 'r') as f:
        lines = f.readlines()
        for line in lines:
            x,y,vx,vy = [int(n) for n in re.findall(r'\d+|\-\d+', line)]
            robots.append([x,y,vx,vy])
    return robots

def solve(robots, R, C, t):
    quads = [0,0,0,0]
    positions = set()
    key = []
    for robot in robots:
        x1,y1,vx,vy = robot
        x2 = (x1 + vx*t)%C
        y2 = (y1 + vy*t)%R
        positions.add((x2,y2))
        key.extend([x2,y2])
        if 0 <= x2 < C//2 and 0 <= y2 < R//2:
            quads[0] += 1
        elif C//2 < x2 < C and 0 <= y2 < R//2:
            quads[1] += 1
        elif 0 <= x2 < C//2 and R//2 < y2 < R:
            quads[2] += 1
        elif C//2 < x2 < C and R//2 < y2 < R:
            quads[3] += 1
    return quads[0]*quads[1]*quads[2]*quads[3], positions, tuple(key)

def pr(positions, R, C):
    out = ''
    for i in range(R):
        for j in range (C):
            if (j,i) in positions:
                out += 'o'
            else:
                out += '.'
        out += '\n'
    print(out)

def find_nn(start, positions, R, C):
    dirs = [(1,0),(0,1),(-1,0),(0,-1)]
    q = deque([(start, 0)])
    visited = set([start])
    while len(q) > 0:
        node, dist = q.popleft()
        x,y = node
        for (dx,dy) in dirs:
            n = (x+dx, y+dy)
            if 0 <= x + dx < C and 0 <= y+dy < R:
                if n in visited:
                    continue
                if n in positions:
                    return dist + 1
                q.append((n,dist+1))
                visited.add(n)
    return None

def get_total_dist(positions, R, C):
    total_dist = 0
    for start in positions:
        total_dist += find_nn(start, positions, R, C)
    return total_dist

if __name__ == "__main__":
    robots = parse('input')
    R = 103
    C = 101
    p1, positions, _ = solve(robots, R, C, 100)
    print(f'Part 1: {p1}')

    t = 0
    states = set()
    key_to_t = {}
    max_iterations = 0
    while True:
        _, pos, key = solve(robots, R, C, t)
        if key in states:
            max_iterations = t
            break
        states.add(key)
        key_to_t[key] = t
        t += 1

    distances = []
    for t in range(0, max_iterations):
        _, pos, key = solve(robots, R, C, t)
        dist = get_total_dist(pos, R, C)
        distances.append((dist, t))

    sort_dist = sorted(distances, key=lambda x: x[0])
    time = sort_dist[0][1]
    print(f'Part 2: {time}')
    _, pos, key = solve(robots, R, C, time)
    pr(pos, R, C)
