
# coding: utf-8

# # Palindrome Number
# Easy
# 
# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
# 
# Example 1:
# 
# Input: 121
# Output: true
# Example 2:
# 
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:
# 
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# In[18]:


def isPalindrome(nums):
    nums = str(nums)
    res = False
    revernums = str()
    if nums[0] == '-':
        res = False

    else:
        revernums = nums[len(nums)::-1]
    
    if revernums ==nums:
        res = True
    
    return res


# In[19]:


nums = 123

print(isPalindrome(nums))

