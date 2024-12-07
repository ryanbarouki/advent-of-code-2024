with open('input.txt', 'r') as f:
    lines = f.readlines()
    blist = []
    alist = []
    for line in lines:
        line = line.strip()
        a,b = line.split()
        alist.append(int(a))
        blist.append(int(b))
    alist = sorted(alist)
    blist = sorted(blist)

    total = 0
    for a, b in zip(alist, blist):
        total += abs(b-a)

    total_2 = 0
    for a in alist:
        total_2 += a*blist.count(a)

    print(f'Part 1: {total}')
    print(f'Part 2: {total_2}')
