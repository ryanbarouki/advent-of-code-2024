import re
from functools import cache

def parse(fname):
    with open(fname, 'r') as f:
        D = f.read().strip().split('\n')
    return D

NUM_PAD = {'7': (0,0), '8': (0,1), '9': (0,2),
           '4': (1,0), '5': (1,1), '6': (1,2),
           '1': (2,0), '2': (2,1), '3': (2,2),
                       '0': (3,1), 'A': (3,2)}

DIR_PAD = {            '^': (0,1), 'A': (0,2),
           '<': (1,0), 'v': (1,1), '>': (1,2)}

@cache
def get_sequence_length(start, end, depth, full_depth):
    pad = NUM_PAD if depth == full_depth else DIR_PAD
    pad_rev = {v:k for k,v in pad.items()}
    si, sj = pad[start]
    i, j = pad[end]
    ud = 'v' if i > si else '^'
    lr = '>' if j > sj else '<'
    uds = abs(si-i)*ud 
    lrs = abs(sj-j)*lr
    if depth == 1:
        ans = len(lrs+uds+'A')
        return ans
    a1 = 0
    a2 = 0
    lrsuds = 'A'+lrs+uds+'A'
    udslrs = 'A'+uds+lrs+'A'
    if (si,j) in pad_rev:
        for k in range(len(lrsuds)-1):
            a1 += get_sequence_length(lrsuds[k], lrsuds[k+1], depth-1, full_depth)
    if (i,sj) in pad_rev:
        for k in range(len(lrsuds)-1):
            a2 += get_sequence_length(udslrs[k], udslrs[k+1], depth-1, full_depth)
    if a1 != 0 and a2 != 0:
        return min(a1, a2)
    elif a1 == 0 and a2 != 0:
        return a2
    elif a2 == 0 and a1 != 0:
        return a1
    return 1

def apply_seq_to_pad(seq, pad):
    pad_rev = {v:k for k,v in pad.items()}
    dirs = {'>':(0,1), '<':(0,-1), '^':(-1,0),'v':(1,0)}
    out = ''
    i, j = pad['A']
    for c in seq:
        if c == 'A':
            out += pad_rev[(i,j)]
            continue
        di, dj = dirs[c]
        i,j = i+di, j+dj
    return out

def find_sequence(code, depth):
    total = 0
    code = 'A'+code
    for i in range(len(code)-1):
        total += get_sequence_length(code[i], code[i+1], depth, depth)
    return total

def solve(codes, depth):
    total = 0
    for code in codes:
        num_part = int(re.findall(r"\d+", code)[0])
        len_sequence = find_sequence(code, depth)
        total += len_sequence*num_part
    return total

if __name__ == "__main__":
    codes = parse('input')
    p1 = solve(codes, depth=3)
    p2 = solve(codes, depth=26)
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")
