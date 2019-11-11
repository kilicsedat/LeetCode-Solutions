#!/usr/bin/env python
# coding: utf-8

# # 3Sum Closest
# Medium
# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
# 
# Example:
# 
# Given array nums = [-1, 2, 1, -4], and target = 1.
# 
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# In[7]:


#import time
def threeSumClosest(nums, target):
    if(len(nums) < 3):
        return 0
    #tic = time.clock()
    nums.sort()
    closest = nums[0] + nums[1] + nums[2]
    i = 0
    while(i < len(nums) - 1):
        a = nums[i]
        j, k = i + 1, len(nums) - 1
        while(j < k):
            b, c = nums[j], nums[k]
            summ = a + b + c
            if(summ == target):
                return summ
            if(abs(target - summ) < abs(target - closest)):
                closest = summ
            if(summ > target):
                k -= 1
            else:
                j += 1
       
        i += 1
    #toc = time.clock()
    #print(toc - tic)
    return closest


# In[8]:


A = [13,2,0,-14,-20,19,8,-5,-13,-3,20,15,20,5,13,14,-17,-7,12,-6,0,20,-19,-1,-15,-2,8,-2,-9,13,0,-3,-18,-9,-9,-19,17,-14,-19,-4,-16,2,0,9,5,-7,-4,20,18,9,0,12,-1,10,-17,-11,16,-13,-14,-3,0,2,-18,2,8,20,-15,3,-13,-12,-2,-19,11,11,-10,1,1,-10,-2,12,0,17,-19,-7,8,-19,-17,5,-5,-10,8,0,-12,4,19,2,0,12,14,-9,15,7,0,-16,-5,16,-12,0,2,-16,14,18,12,13,5,0,5,6]
t = -59
print(threeSumClosest(A,t))


# In[ ]:




