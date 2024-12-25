from collections import defaultdict

def parse(fname):
    with open(fname, 'r') as f:
        locks_keys = f.read().strip().split('\n\n')
    locks = []
    keys = []
    for lk in locks_keys:
        if lk[0] == "#":
            locks.append(lk.strip())
        elif lk[0] == '.':
            keys.append(lk.strip())
    return locks, keys

def grid_to_counts(grid):
    rows = grid.split('\n')
    cols = defaultdict(int)
    for i in range(len(rows)):
        for j in range(len(rows[0])):
            if rows[i][j] == '#':
                cols[j] += 1
    return [cols[k]-1 for k in range(5)]

def solve(locks, keys):
    count = 0
    for lock in locks:
        for key in keys:
            lock_counts = grid_to_counts(lock)
            key_counts = grid_to_counts(key)
            skip = False
            for i, lc in enumerate(lock_counts):
                if 5-lc < key_counts[i]:
                    skip = True
                    break
            if not skip:
                count += 1
    return count

if __name__ == "__main__":
    locks, keys = parse('input')
    p1 = solve(locks, keys)
    print(f"Merry Christmas: {p1}")
