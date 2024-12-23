from collections import defaultdict, deque
from io import SEEK_END
from tqdm import tqdm

def parse(fname):
    adj = defaultdict(set)
    with open(fname, 'r') as f:
        for l in f.readlines():
            c1,c2 = l.strip().split('-')
            adj[c1].add(c2)
            adj[c2].add(c1)
    return adj

def ordered(path):
    return ",".join(sorted(path))

def get_neighbours(node, adj, path):
    ns = []
    for n in adj[node]:
        skip = False
        for nn in path:
            if n not in adj[nn]:
                skip = True
                break
        if skip:
            continue
        ns.append(n)
    return ns

def dfs_p1(start, adj):
    q = deque([(start, 0, [start])])
    seen_groups = set()
    while q:
        node, depth, path = q.pop()
        opath = ordered(path)
        if depth == 2:
            if opath in seen_groups:
                continue
            seen_groups.add(opath)
            yield path
            continue
        for n in get_neighbours(node, adj, path):
            q.append((n,depth+1,path+[n]))

def dfs2_p2(start, adj):
    q = deque([(start, 0, [start])])
    seen_groups = set()
    while q:
        node, depth, path = q.pop()
        opath = ordered(path)
        if opath in seen_groups:
            continue
        seen_groups.add(opath)
        ns = get_neighbours(node, adj, path)
        if len(ns) == 0:
            yield path
            continue
        for n in ns:
            q.append((n,depth+1,path+[n]))
        
def part1(adj):
    tset = set()
    for c in adj:
        if c[0] == 't':
            tset.add(c)
    count_groups = 0
    oset = set()
    for tc in tset:
        for group in dfs_p1(tc, adj):
            count_groups += 1
            oset.add(ordered(group))
    return len(oset)

def part2(adj):
    oset = set()
    biggest = ''
    max = 0
    for c in tqdm(adj):
        for group in dfs2_p2(c, adj):
            ogroup = ordered(group)
            if ogroup in oset:
                continue
            if len(group) > max:
                biggest = ogroup
                max = len(group)
            oset.add(ogroup)
    return biggest

if __name__ == "__main__":
    adj = parse('input')
    p1 = part1(adj)
    print(f"Part 1: {p1}")
    p2 = part2(adj)
    print(f"Part 2: {p2}")
            
