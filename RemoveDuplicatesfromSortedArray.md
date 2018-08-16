---
layout: post
title: "Remove Duplicates from Sorted Array"
author: poanchen
date: 2018-08-15 08:30:30
source: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
tags:
- Array
- In-place
technics:
- Two Pointers
- Slow and Fast Pointers
---

Input: arr = [0,0,1,1,1,2,2,3,3,4]

Output: 5 (size of [0,1,2,3,4])

Solution:
Have a slow and fast pointer that was initialized to 0 and 1 respectively. Keep incrementing fast pointer until arr[slow] != arr[fast]. When that happens, replace the arr[slow + 1] as arr[fast]. Then you may increment both the slow and fast pointer by 1.

Runtime: O(n), O(1)
