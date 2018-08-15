---
layout: post
title: "Product of Array Except Self"
author: poanchen
date: 2018-08-15 08:30:30
source: https://leetcode.com/problems/product-of-array-except-self/description/
tags:
- Array
technics:
- RunningSum
---

Input: arr = [2,3,6,4]

Output: [72,48,24,36]

Solution:
Do running multiplication from left to right first, and right to left as well. For each iteration, you should be able to know the product of array except self by looking up the running multiplication arrays. For example, left to right would be [2,6,36,72] and right to left would be [144,72,24,4]. To get 3rd index (24), you do 6 * 4.

Runtime: O(n), O(n)
