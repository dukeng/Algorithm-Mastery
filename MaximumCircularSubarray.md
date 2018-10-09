---
layout: post
title: "Max Circular Sum Subarray"
author: dukeng
date: 2018-08-15 08:30:30
source: https://leetcode.com/problems/maximum-sum-circular-subarray/

Topic:
- Array

tags:
- Subarray
technics:
- Kadane's algorithm
- Divide and Conquer
- DP
---

Input: [3,-2,2,-3]

Output: Subarray [3] and [3,-2,2] both have maximum sum 3

Solution:
There are 2 cases: one case is subarray is one interval. 2nd case is subarray is two interval.

For one interval, just run Kadane algorithm.
For two interval, have an O(N) running sum from right to left, then compute max_sum[i] in range(len(A) -1, 0)
Then compare running_sum_from_left + max_running_sum_from_right with one interval sum.

Runtime: O(n), O(n)

Note:
There are other Solutions with constant space.

Code:
```
    def maxSubarraySumCircular(self, A):
        N = len(A)

        ans = cur = None
        for x in A:
            cur = x + max(cur, 0)
            ans = max(ans, cur)

        # ans is the answer for 1-interval subarrays.
        # Now, let's consider all 2-interval subarrays.
        # For each i, we want to know
        # the maximum of sum(A[j:]) with j >= i+2

        # rightsums[i] = sum(A[i:])
        rightsums = [None] * N
        rightsums[-1] = A[-1]
        for i in xrange(N-2, -1, -1):
            rightsums[i] = rightsums[i+1] + A[i]

        # maxright[i] = max_{j >= i} rightsums[j]
        maxright = [None] * N
        maxright[-1] = rightsums[-1]
        for i in xrange(N-2, -1, -1):
            maxright[i] = max(maxright[i+1], rightsums[i])

        leftsum = 0
        for i in xrange(N-2):
            leftsum += A[i]
            ans = max(ans, leftsum + maxright[i+2])
        return ans
```        
