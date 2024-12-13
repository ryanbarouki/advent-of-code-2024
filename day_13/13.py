import re
from collections import defaultdict
def parse(fname):
    with open(fname, 'r') as f:
        examples = []
        D = f.read().strip().split('\n\n')
        for example in D:
            ex = defaultdict(list)
            for i, line in enumerate(example.split('\n')):
                x, y = re.findall(r'\d+', line)
                x,y = int(x), int(y)
                if i < 2:
                    ex['bases'].append([x,y])
                else:
                    ex['target'] = [x,y]
            examples.append(ex)

    return examples

def inverse_matrix(mat):
    a, b, c, d = mat[0][0], mat[0][1], mat[1][0], mat[1][1]
    det = a*d - b*c
    if det == 0:
        return None
    return [[d, -b], [-c, a]], det

def matmul(mat, v):
    res = [0]*len(mat[0])
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            res[i] += mat[i][j]*v[j]
    return res

def solve(examples, part2=False):
    total = 0
    for ex in examples:
        va, vb = ex['bases']
        xa, ya = va
        xb, yb = vb
        x,y = ex['target']
        if part2:
            x += 10000000000000
            y += 10000000000000
        mat = [[xa, xb], [ya, yb]]
        inv = inverse_matrix(mat)
        if inv is None:
            continue
        det_times_imat, det = inv
        a1, a2 = matmul(det_times_imat, [x,y]) 
        # avoid floating point BS
        if a1 % det != 0 or a2 % det != 0:
            continue
        a1, a2 = a1//det, a2//det
        total += 3*a1 + a2
    return total

if __name__ == "__main__":
    examples = parse('input')
    print(f'Part 1: {solve(examples)}')
    print(f'Part 2: {solve(examples, part2=True)}')
    solve(examples)
