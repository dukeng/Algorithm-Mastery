---
layout: post
title: "Find (maximum length/all) of subarray given sum"
author: dukeng
date: 2018-08-14 08:30:30
source: http://www.techiedelight.com/find-maximum-length-sub-array-having-given-sum/
tags:
- HashSet
- HashMap
- Array
technics:
- Running Sum
---

Input: arr = [5,6,-5,5,2,5,3,-2, 0], sum = 8 

Output: 4 because {-5,5,3,5}. Could be {5,3} but {-5,5,3,5} is longer

Solution: do a running sum hashMap with {key: running sum, value: index} for the array while checking if current_sum - sum exists in the hashMap. To find all subarray, store the value as a list of indexes.

Runtime: O(n), O(n)
