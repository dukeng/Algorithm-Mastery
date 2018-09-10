---
layout: post
title: "RLE Iterator"
author: poanchen
date: 2018-09-10 08:30:30
source: https://leetcode.com/problems/rle-iterator/description/
tags:
- Array
technics:
- Just do it
---

Input: arr = ["RLEIterator","next","next","next","next"], [[[3,8,0,9,2,5]],[2],[1],[1],[2]]

Output: [null,8,8,5,-1]

Explanation: 
RLEIterator is initialized with RLEIterator([3,8,0,9,2,5]).
This maps to the sequence [8,8,8,5,5].
RLEIterator.next is then called 4 times:

.next(2) exhausts 2 terms of the sequence, returning 8.  The remaining sequence is now [8, 5, 5].

.next(1) exhausts 1 term of the sequence, returning 8.  The remaining sequence is now [5, 5].

.next(1) exhausts 1 term of the sequence, returning 5.  The remaining sequence is now [5].

.next(2) exhausts 2 terms, returning -1.  This is because the first term exhausted was 5,
but the second term did not exist.  Since the last term exhausted does not exist, we return -1.

Solution:
Keep counting arr[i] when i is even. When number(s) are exhausts, check to see if it is still within the range, if it is, simply returns the arr[i+1], or simply keep counting to the next one until you reached the point (return arr[i+1]) or out of bounce (return -1).

Runtime: O(n), O(n)
