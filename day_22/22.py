def parse(fname):
    with open(fname, 'r') as f:
        D = [int(num) for num in f.read().strip().split('\n')]
    return D

def mix(n1, n2):
    return n1 ^ n2

def prune(num):
    return num % 16777216

def step(num):
    res = num*64
    num = mix(num, res)
    num = prune(num)
    res = num//32
    num = mix(num, res)
    num = prune(num)
    res = num*2048
    num = mix(num, res)
    num = prune(num)
    return num

def part1(nums):
    total = 0
    cache = {}
    for num in nums:
        diffs = []
        last_ones = ones(num)
        og_num = num
        for i in range(2000):
            num = step(num)
            curr_ones = ones(num)
            diff = curr_ones-last_ones
            diffs.append(diff)
            last_ones = curr_ones
            if i >= 3:
                i1, i2, i3, i4 = diffs[i-3:i+1]
                if (i1,i2,i3,i4,og_num) not in cache:
                    cache[(i1,i2,i3,i4,og_num)] = curr_ones
        total += num
    return total, cache

def ones(num):
    return num%10

def part2(nums, cache):
    done = set()
    max_total = 0
    for item in cache:
        i1,i2,i3,i4,_ = item
        if (i1,i2,i3,i4) in done:
            continue
        total = 0
        for num in nums:
            if (i1,i2,i3,i4,num) in cache:
                total += cache[(i1,i2,i3,i4,num)]
        if total > max_total:
            max_total = total
        done.add((i1,i2,i3,i4))
    return max_total

if __name__ == "__main__":
    nums = parse('input')
    p1, cache = part1(nums)
    print(f"Part 1: {p1}")
    p2 = part2(nums, cache)
    print(f"Part 2: {p2}")
