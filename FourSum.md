---
layout: post
title: "4 Sum"
author: dukeng
date: 2018-08-14 08:30:30
source: http://www.techiedelight.com/4-sum-problem/
tags:
- HashSet
- HashMap
- Array
- SubSet
technics:
- Two Sum
---

Input: arr = [ 2, 7, 4, 0, 9, 5, 1, 3]

Output: (0, 4, 7, 9), (1, 3, 7, 9), (2, 4, 5, 9)

Solution: Go through a nested loop (index i and j) and maintain a hashMap containing all possible two sum. As we go check if the remaining sum is in the hashMap. After that need to verify that i and j is different from the sum that we see

Runtime: O(n^3), O(n^2)
