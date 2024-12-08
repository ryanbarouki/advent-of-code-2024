import itertools

def parse(fname):
    with open(fname) as f:
        lines = f.readlines()
        checksums = []
        inputs = []
        for line in lines:
            checksum, nums = line.strip().split(':')
            checksum = int(checksum)
            nums = [int(num) for num in nums.strip().split(' ')]
            inputs.append(nums)
            checksums.append(checksum)
        return checksums, inputs

def count_valid_sums(checksums, inputs, ops):
    count = 0
    for i, nums in enumerate(inputs):
        checksum = checksums[i]
        for perm in itertools.product(ops.keys(), repeat=len(nums)-1):
            running_sum = 0
            n = nums[0]
            for j in range(len(nums)-1):
                op = ops[perm[j]]
                next = nums[j+1]
                running_sum = op(n, next)
                n = running_sum
            if running_sum == checksum:
                count += checksum
                break
    return count


ops1 = {'+': lambda a,b: a+b, '*': lambda a,b: a*b}
ops2 = {**ops1, '||': lambda a,b: int(f'{a}{b}')}

checksums, inputs = parse('input')
print(f'Part 1: {count_valid_sums(checksums, inputs, ops1)}')
print(f'Part 2: {count_valid_sums(checksums, inputs, ops2)}')
# part1(checksums, inputs)
