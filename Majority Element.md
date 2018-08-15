---
layout: post
title: "Find the element in array that appears more than ⌊n/2⌋ times"
author: poanchen
date: 2018-08-15 08:30:30
source: https://leetcode.com/problems/majority-element/description/
tags:
- Array
- HashMap
- Sorting
- Randomization
- Divide and Conquer
- Boyer-Moore Voting Algorithm
technics:
---

Input: arr = [2,2,1,1,1,2,2]

Output: 2

Solution:
Loop through the whole array, set the first element in the array as candidate, whenever you see a different number than a candidate, you minus the count by one until when count reaches zero, you set the next element as candidate. Or whenever you see the candidate number again, you plus the count by one. At the end, the candidate should be the answer.

Runtime: O(n), O(1)
