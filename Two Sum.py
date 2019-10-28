#!/usr/bin/env python
# coding: utf-8

# # Two Sum
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].

# In[ ]:


from itertools import combinations
import numpy as np
nums = [2, 7, 11, 7, 15]
target = 9

class Solution:
    def twoSum(self, nums, target):
        index_map = {}
        for i in range(len(nums)):
            num = nums[i]
            pair = target - num
            if pair in index_map:
                return [index_map[pair], i]
            index_map[num] = i
        return None 

