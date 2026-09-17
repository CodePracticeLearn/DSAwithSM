# 875. Koko Eating Bananas

`Medium` · `Binary Search`

🔗 **[Problem on LeetCode](https://leetcode.com/problems/koko-eating-bananas/)**

## Problem

Koko loves to eat bananas. There are n piles of bananas, the i-th pile has piles[i] bananas. The guards have gone and will come back in h hours. Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. She can finish the pile in one sitting if it's smaller. Return the minimum integer k such that she can eat all the bananas within h hours.

## Solution

See [`solution.py`](./solution.py) — verified by [`test_solution.py`](./test_solution.py).

```bash
python -m pytest test_solution.py
```

Primary function: `min_eating_speed`
