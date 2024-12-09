def parse(fname):
    with open(fname) as f:
        D = f.read().strip()
    return D

def preprocess(data):
    disk = [] 
    free = []
    pos = 0
    contig_size = 0
    max_fname = 0
    sizes = {}
    for i, size in enumerate(data):
        size = int(size)
        if i % 2 == 0:
            filename = i//2
            contig_size += size
            sizes[filename] = size
            if filename > max_fname:
                max_fname = filename
        else:
            filename = '.'
            free.extend([j for j in range(pos, pos+size)])
        disk.extend([filename]*size)
        pos += size
    return [str(k) for k in disk], free, contig_size, max_fname, sizes

def part1(disk, free, contig_size):
    free = free[::-1]
    while len(free) > 0:
        for i in range(len(disk)-1, -1, -1):
            fname = disk[i]
            if fname != '.':
                if i == contig_size - 1:
                    return [(j, int(fname)) for j, fname in enumerate(disk) if fname != '.']
                freepos = free.pop()
                disk[freepos] = fname
                disk[i] = '.'
                break
    return [(j, int(fname)) for j, fname in enumerate(disk) if fname != '.']

def get_leftmost_free_size(disk):
    size = 0
    free_blocks = []
    for i, fname in enumerate(disk):
        if fname != '.' and size > 0:
            free_blocks.append((i-size, size))
            size = 0
        elif fname == '.':
            size += 1
    return free_blocks

def move(free_blocks, disk, fname, i):
    for free in free_blocks:
        start_id, size = free
        if sizes[fname] > size:
            continue
        if start_id + size > i:
            continue
        disk[start_id:start_id+sizes[fname]] = [fname]*sizes[fname]
        disk[i-sizes[fname]+1:i+1] = ['.']*sizes[fname]
        return

def part2(disk, max_fname, sizes):
    for fname in range(max_fname, -1, -1):
        free_blocks = get_leftmost_free_size(disk)
        for i in range(len(disk)-1, -1, -1):
            name = disk[i]
            if name == '.' or int(name) != fname:
                continue
            move(free_blocks, disk, fname, i)
            break
    return [(j, int(fname)) for j, fname in enumerate(disk) if fname != '.']


def get_checksum(disk):
    checksum = 0
    for i, fname in disk:
        checksum += i*int(fname)
    return checksum


data = parse('input')
disk, free, contig_size, max_fname, sizes = preprocess(data)
# print(''.join(disk))
# print(f'Part 1: {get_checksum(part1(disk, free, contig_size))}')
print(f'Part 2: {get_checksum(part2(disk, max_fname, sizes))}')
