---
layout: post
title: "Move all zeros in the array to the far right while preserving the order of all non-zero number"
author: poanchen
date: 2018-08-15 08:30:30
source: https://leetcode.com/problems/move-zeroes/description/
tags:
- Array
- In-place
technics:
- Two Pointers
---

Input: arr = [0,1,0,3,12]

Output: [1,3,12,0,0]

Solution:
Initialize a variable named lastSeenNonZeroIndex and set it to 0. Loop through the array, whenever you see a non-zero number, you swap it with the index lastSeenNonZeroIndex. Increment lastSeenNonZeroIndex by one. Whenever you see a number zero, you simply carry on.

Runtime: O(n), O(1)
