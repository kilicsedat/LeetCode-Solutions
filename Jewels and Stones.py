
# coding: utf-8

# # Jewels and Stones
# Easy
# 
# You're given strings J representing the types of stones that are jewels, and S representing the stones you have. Each character in S is a type of stone you have. You want to know how many of the stones you have are also jewels.
# 
# The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".
# 
# Example 1:
# 
# Input: J = "aA", S = "aAAbbbb" Output: 3 Example 2:
# 
# Input: J = "z", S = "ZZ" Output: 0 Note:
# 
# S and J will consist of letters and have length at most 50. The characters in J are distinct.

# In[8]:


def countJewels(j, s):
    return sum(x in j for x in s)


# In[9]:


J = "aAb"
S = "aAAbbbbBBB"

print (countJewels(J, S))


# In[10]:


n1 = [1, 2]
n2 = [3, 4, 5, 2]

print (countJewels(n1, n2))

