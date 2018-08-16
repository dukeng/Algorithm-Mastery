---
layout: post
title: "Merge Sorted Array"
author: poanchen
date: 2018-08-15 08:30:30
source: https://leetcode.com/problems/merge-sorted-array/description/
tags:
- Array
- Sorted
- Ad hoc
technics:
- Two Pointers
---

Input: arr1 = [1,2,3,0,0,0], arr2 = [4,5,6]

Output: [1,2,3,4,5,6]

Solution:
Used two pointers from back of both arrays. Compare them and keep pushing the larger value to the back of the longer array.

Runtime: O(n), O(1)
