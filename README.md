# 📦 Partition Array Into K-Distinct Groups

This repository contains a Python solution to **LeetCode Weekly Contest 464 – Question 2: Partition Array Into K-Distinct Groups**.

---

## 🧠 Problem Summary

You are given an integer array `nums` and an integer `k`.  
Your task is to determine whether it is possible to partition all elements of `nums` into one or more groups such that:

- Each group contains exactly `k` **distinct** elements.
- Each element in `nums` must be assigned to **exactly one group**.

Return `True` if such a partition is possible, otherwise return `False`.

---

## ✅ Approach

This solution uses a **frequency counter + heap-based greedy strategy** to:

- Track how many times each value appears
- Form groups of `k` distinct values while respecting element counts
- Ensure all elements are used exactly once

### Key Techniques

- `collections.Counter` for frequency mapping
- `heapq` for efficient selection of available values
- Greedy group formation with backtracking fallback

---
## 🧪 Example Test Cases
Input: nums = [1, 2, 3, 4], k = 2
Output: True
# Groups: [1, 2], [3, 4]

Input: nums = [3, 5, 2, 2], k = 2
Output: True
# Groups: [2, 3], [2, 5]

Input: nums = [1, 5, 2, 3], k = 3
Output: False
# Cannot form groups of 3 distinct elements using all values

## 📊 Complexity

```markdown
Time Complexity: O(n log d)
- n = total number of elements
- d = number of distinct values

Space Complexity: O(d)
- Frequency map and heap
