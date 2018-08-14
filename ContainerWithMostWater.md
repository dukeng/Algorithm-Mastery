---
layout: post
title: "Container with most water"
author: dukeng
date: 2018-08-14 08:30:30
source: https://leetcode.com/problems/container-with-most-water/description/
tags:
- Array
- Greedy
technics:
- Two Pointer
---

Input: [1,8,6,2,5,4,8,3,7]

Output: 49

Solution: 
maintain 2 pointers left(L) and right(R).
While L < R:
  Update the max area as you go. 
  Move the pointer with lower value (L goes right, R goes L) until there is a value that is higher than the current lower.

Runtime: O(n), O(1)
