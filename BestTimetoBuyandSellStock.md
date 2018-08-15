---
layout: post
title: "Best Time to Buy and Sell Stock"
author: poanchen
date: 2018-08-15 08:30:30
source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
tags:
- Array
- DP
technics:
---

Input: arr = [7,1,5,3,6,4]

Output: 5 (Buy at 1 and sell at 6 to get profit of 5)

Solution:
Initialize two variables of maxProfit and min where maxProfit keeps track of the largest profit we have seen and the min stores the minimum number that we have seen so far. Loop through the array, whenever we see a number that is smaller than our min, we update it. For every iteration, We also check that if we sell the stock now, do we get a better profit? if we do, update it otherwise keep going.

Runtime: O(n), O(1)
