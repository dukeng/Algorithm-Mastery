---
layout: post
title: "Find all distinct pairs with given differences in an array"
author: dukeng
date: 2018-08-14 08:30:30
tags:
- HashSet
- HashMap
- Array
- SubSet
technics:
- Two Sum
---

Input: arr = [1,5,2,2,2,5,5,4] target = 3

Output: (2,5) and (1,4)

Solution: put each arr[i] for i in [0, len(arr)] in a hashMap and check if arr[i] +/- target exists in hashMap

Runtime: O(n), O(n)
