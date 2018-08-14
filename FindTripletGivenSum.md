---
layout: post
title: "Find Triplet in array with the given sum"
author: dukeng
date: 2018-08-14 08:30:30
source: http://www.techiedelight.com/find-triplet-given-with-given-sum/
tags:
- HashSet
- HashMap
- Array
technics:
- Running Sum
---

Input: arr = [ 2, 7, 4, 0, 9, 5, 1, 3 ], sum = 6

Output: Triplet (0 1 5) (0 2 4) (1 2 3)

Solution: Insert each element of the array in HashMap { key: arr[i], value: set of i}.
Consider all pairs in the array O(n^2) and check if remaining sum in map or no. If remaining sum is seen and triple don't overlap then that's the triplet

Runtime: O(n^2), O(n)
