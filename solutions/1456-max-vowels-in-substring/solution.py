def max_vowels(s, k):
    vowels = set("aeiou")
    count = sum(1 for c in s[:k] if c in vowels)
    best = count
    for i in range(k, len(s)):
        count += (1 if s[i] in vowels else 0) - (1 if s[i - k] in vowels else 0)
        best = max(best, count)
    return best
