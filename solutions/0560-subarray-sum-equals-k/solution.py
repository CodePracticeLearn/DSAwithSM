from collections import defaultdict


def subarray_sum(nums, k):
    prefix = defaultdict(int)
    prefix[0] = 1
    total = 0
    count = 0
    for n in nums:
        total += n
        count += prefix[total - k]
        prefix[total] += 1
    return count
