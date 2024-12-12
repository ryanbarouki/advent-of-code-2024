def parse(fname):
    with open(fname) as f:
        D = f.read().strip().split(' ')
    return D

def apply_rules(num):
    inum = int(num)
    if inum == 0:
        return '1',
    elif len(num) % 2 == 0:
        return str(int(num[:len(num)//2])), str(int(num[len(num)//2:]))
    else:
        return str(inum*2024),


def memoize(function):
    memo = {}
    def wrapper(*args):
        num, its, total_its= args
        if (num, total_its-its) in memo:
            return memo[(num, total_its-its)]
        else:
            v = function(*args)
            memo[(num, total_its-its)] = v
            return v
    return wrapper

@memoize
def rules_recursion(num, its, total_its):
    count = 0
    if its == total_its:
        return 1
    for n in apply_rules(num):
        count += rules_recursion(n, its+1, total_its)
    return count

nums = parse('input')

count = 0
for num in nums:
    count += rules_recursion(num, 0, 25)
print(f'Part 1: {count}')

count = 0
for num in nums:
    count += rules_recursion(num, 0, 75)
print(f'Part 2: {count}')
