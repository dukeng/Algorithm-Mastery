---
layout: post
title: "Largest subarray with equal # of 0s and 1s"
author: dukeng
date: 2018-08-14 08:30:30
source: https://www.geeksforgeeks.org/largest-subarray-with-equal-number-of-0s-and-1s/
tags:
- HashSet
- HashMap
- Array
- Subarray
technics:
- Running Sum
---

Input: arr = {0,0,1,0,1,0,0} 

Output: {0,1,0,1} or {1,0,1,0} 

Solution: Turn every 0 to -1. Traverse the array and store the sum of elements so far. 
  If sum is 1st time seen, make { key: sum, value index} 
  If the sum at index i is already seen at index j, that means from [i,j] it's going to be 0. Update the length if needed. 

Runtime: O(n), O(n)
