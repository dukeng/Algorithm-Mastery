---
layout: post
title: "Max Sum Subarray"
author: poanchen
date: 2018-08-15 08:30:30
source: https://leetcode.com/problems/maximum-subarray/description/

Topic:
- Array

tags:
- Subarray
technics:
- Kadane's algorithm
- Divide and Conquer
---

Input: [-2,1,-3,4,-1,2,1,-5,4]

Output: 6 since [4,-1,2,1] has the largest sum = 6.

Solution:
Initialize two variables, currentSum and maxSum and set maxSum to be Integer.MIN and not 0 since maxSum could have negative value;
Loop from [0, len(arr)]
  Add current value to currentSum
  Update the maxSum as you go.
  Whenever the currentSum became negative number, we reset our currentSum to zero. // The rational behind this is that in order to find the max sum, we need to be greedy. Any sum that ends with negative number, we should reset this since there might be better sum after this.

Runtime: O(n), O(1)

Code:
```
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentSum = 0
        maxSum = -sys.maxsize
        for num in nums:
            currentSum += num
            maxSum = max(maxSum, currentSum)
            if currentSum < 0:
                currentSum = 0
        return maxSum
```        
