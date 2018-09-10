---
layout: post
title: "Online Stock Span"
author: poanchen
date: 2018-09-10 08:30:30
source: https://leetcode.com/problems/online-stock-span/description/
tags:
- Array
technics:
- Greedy
- Max/Min Stack
---

Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]

Output: [null,1,1,1,2,1,4,6]

Explanation: 
First, S = StockSpanner() is initialized.  Then:
S.next(100) is called and returns 1,
S.next(80) is called and returns 1,
S.next(60) is called and returns 1,
S.next(70) is called and returns 2,
S.next(60) is called and returns 1,
S.next(75) is called and returns 4,
S.next(85) is called and returns 6.

Note that (for example) S.next(75) returned 4, because the last 4 prices
(including today's price of 75) were less than or equal to today's price.

Solution:
Keep a Min Stack. Whenever it is not empty, you keep popping whenever the minimum number in stack is smaller or equal to the current number or became empty again. And then, you push it to the stack. In this way, we have a sorted stack where the next number to be poped will the the smallest number while the bottomest will be the largest number. While we pop it, we keep adding the result so that we can return later.

Runtime: O(n), O(n)
