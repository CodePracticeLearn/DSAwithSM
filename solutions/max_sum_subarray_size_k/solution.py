def max_sum_subarray_k(nums, k):
    if k <= 0 or k > len(nums):
        return 0
    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        best = max(best, window)
    return best
