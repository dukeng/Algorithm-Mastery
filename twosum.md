---
layout: post
title: "Find pair with given sum in an array"
author: dukeng
date: 2018-08-14 08:30:30
tags:
- HashSet
- HashMap
- Array
technics:
- Two Sum
---

Input: arr = [2, 7, 11, 15] target = 9

Output: arr[0] + arr[1] = 2 + 7 = 9 -> [0,1]

Solution: put each arr[i] for i in [0, len(arr)] in a hashMap and check if target - arr[i] exists in hashMap
