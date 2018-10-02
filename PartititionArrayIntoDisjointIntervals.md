---
layout: post
title: "Partition Array into Disjoint Intervals"
author: poanchen
date: 2018-08-15 08:30:30
source: https://leetcode.com/contest/weekly-contest-104/problems/partition-array-into-disjoint-intervals/
tags:
- Array

technics:
- minmax
---

Input: arr = [5,0,3,8,6]

Description: partition arr into 2 subarrays so that:
1. Every element of left is less than element of right
2. Left and Right are non-empty
3. Left has the smallest possible size

Output: left = [5,0,3], right = [8,6]

Solution:
Create a running min array from right to left, create a running max from left to right. Loop through from left to right and return index when max[index] <= min[index+1]

Runtime: O(n), O(n)
