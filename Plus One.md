---
layout: post
title: "Plus One"
author: poanchen
date: 2018-08-14 08:30:30
source: https://leetcode.com/problems/plus-one/description/
tags:
- Array
- Math
technics:
- Modules
---

Input: arr = [1,2,3]

Output: [1,2,4] as [1,2,3] represents integer 123 and plus one of that is 124

Solution:
Loop from the back of the array and add one to it. Keep doing it until the remainder is zero. When overflow happens, simply create an array of size len(arr) + 1 and set the first digit to 1 and return it.

Runtime: O(n), O(1)
