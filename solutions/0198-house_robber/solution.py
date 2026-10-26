def rob(nums):
    rob1, rob2 = 0, 0
    for n in nums:
        new_rob = max(rob1 + n, rob2)
        rob1 = rob2
        rob2 = new_rob
    return rob2
