#!/usr/bin/env python
# coding: utf-8

# # Split a String in Balanced Strings
# Easy
# 
# Balanced strings are those who have equal quantity of 'L' and 'R' characters.
# 
# Given a balanced string s split it in the maximum amount of balanced strings.
# 
# Return the maximum amount of splitted balanced strings.
# 
#  
# 
# Example 1:
# 
# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
# Example 2:
# 
# Input: s = "RLLLLRRRLR"
# Output: 3
# Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
# Example 3:
# 
# Input: s = "LLLLRRRR"
# Output: 1
# Explanation: s can be split into "LLLLRRRR".
# Example 4:
# 
# Input: s = "RLRRRLLRLL"
# Output: 2
# Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'
#  

# In[10]:


def balancedStringSplit(s):
    num, L_num, R_num = 0, 0, 0
    for x in s:
        if x == 'L':
            L_num += 1
        else:
            R_num += 1
        if L_num == R_num:
            num += 1
    return num


# In[11]:


s = 'LLRRLR'

print(balancedStringSplit(s))
        


# In[ ]:




