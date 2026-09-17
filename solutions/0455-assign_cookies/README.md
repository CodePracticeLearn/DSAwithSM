# 455. Assign Cookies

`Easy` · `Greedy`

🔗 **[Problem on LeetCode](https://leetcode.com/problems/assign-cookies/)**

## Problem

Assume you are an awesome parent and want to give your children some cookies. Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with. Each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

## Solution

See [`solution.py`](./solution.py) — verified by [`test_solution.py`](./test_solution.py).

```bash
python -m pytest test_solution.py
```

Primary function: `find_content_children`
