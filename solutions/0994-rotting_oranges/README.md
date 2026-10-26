# 994. Rotting Oranges

`Medium` · `Graphs`

📺 **[Watch the walkthrough on YouTube](https://youtu.be/eCTcdtj5aZg)**

🔗 **[Problem on LeetCode](https://leetcode.com/problems/rotting-oranges/)**

## Problem

You are given an m x n grid where each cell can have value 0 (empty), 1 (fresh orange), or 2 (rotten orange). Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten. Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

## Solution

See [`solution.py`](./solution.py) — verified by [`test_solution.py`](./test_solution.py).

```bash
python -m pytest test_solution.py
```

Primary function: `oranges_rotting`
