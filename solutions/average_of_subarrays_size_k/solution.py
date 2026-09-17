def average_subarrays_k(nums, k):
    res = []
    window = 0.0
    for i, x in enumerate(nums):
        window += x
        if i >= k - 1:
            res.append(window / k)
            window -= nums[i - k + 1]
    return res
