from collections import Counter


def character_replacement(s, k):
    count = Counter()
    left = 0
    max_freq = 0
    best = 0
    for right, c in enumerate(s):
        count[c] += 1
        max_freq = max(max_freq, count[c])
        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best
