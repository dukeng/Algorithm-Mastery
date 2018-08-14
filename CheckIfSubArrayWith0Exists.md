---
layout: post
title: "Check if a subarray with sum = 0 exists in an array"
author: dukeng
date: 2018-08-14 08:30:30
source: http://www.techiedelight.com/check-subarray-with-0-sum-exists-not/
tags:
- HashSet
- HashMap
- Array
- SubArray
technics:
- Running Sum
---

Input: arr = {1,2,4,6,3,-3,-6,6,-3}

Output: yes because {6,3,-3,-6}

Solution: do a running sum hashMap with {key: running sum, value: index} for the array while checking if current_sum == 0 or current_sum exists in the hashMap. To find all subarray, store the value as a list of indexes.

Runtime: O(n), O(n)
