---
layout: post
title: "Word Search"
author: poanchen
date: 2018-08-15 08:30:30
source: https://leetcode.com/problems/word-search/description/
tags:
- Array
- 2D Array
- String
- Backtracking
technics:
- DFS
---

Input:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED"

Output: true

Solution:
Double for loop, for each iteration, you do a DFS for every possible ways (up, down, left and right). While doing DFS, you apply the backtracking technics to make sure you do not visit the path that you have seen before. Basically try everything.

Runtime: O(n * m * 4^k), O(1) where n is the rows size, m is the cols size, and k is the length of the word to search for
