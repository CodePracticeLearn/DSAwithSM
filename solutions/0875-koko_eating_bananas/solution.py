import math

def min_eating_speed(piles, h):
    left, right = 1, max(piles)
    result = right
    while left <= right:
        k = (left + right) // 2
        hours = sum(math.ceil(p / k) for p in piles)
        if hours <= h:
            result = k
            right = k - 1
        else:
            left = k + 1
    return result
