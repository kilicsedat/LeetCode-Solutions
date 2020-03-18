#!/usr/bin/env python
# coding: utf-8

# # Find First and Last Position of Element in Sorted Array
# Medium
# 
# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# If the target is not found in the array, return [-1, -1].
# 
# Example 1:
# 
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
# 
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# In[2]:


import bisect
def searchRange(nums,target):
    s = bisect.bisect_left(nums, target)
    e = bisect.bisect_left(nums, target+1)-1
    return [s,e] if s < len(nums) and nums[s]==target else [-1,-1]


# In[3]:


nums, target = [5,7,7,8,8,10],  8
print(searchRange(nums, target))


# In[ ]:




