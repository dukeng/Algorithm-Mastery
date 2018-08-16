---
layout: post
title: "Search in Rotated Sorted Array"
author: poanchen
date: 2018-08-15 08:30:30
source: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
tags:
- Array
- Sorted
- Binary Search
technics:
---

Input: arr = [4,5,6,7,0,1,2], target = 0

Output: 4 (index)

Solution:
Do binary search with low and high pointer. Check if low to mid is increasing, if the target is within the low to mid range, then it is on the left otherwise it is on the right. Else check if mid to high is increasing, if the target is within the mid to high range, then it is on the right otherwise it is on the left.

Runtime: O(logn), O(1)
