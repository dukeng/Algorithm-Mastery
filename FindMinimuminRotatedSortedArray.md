---
layout: post
title: "Find Minimum in Rotated Sorted Array"
author: poanchen
date: 2018-08-16 08:30:30
source: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
tags:
- Sorted
technics:
- Binary Search
---

Input: arr = [3,4,5,1,2]

Output: 1 (smallest element in the array)

Solution:
Start low at far left and high at far right. To detect bottom, simply check if arr[mid] > arr[mid + 1] is true. Then return arr[mid + 1]. Then check if arr[low] < arr[mid] is true then the minimum could be on the right side. Else the minimum could be on the left side. If no bottom of mountain is found, then the answer should be arr[0]

Runtime: O(logn), O(1)
