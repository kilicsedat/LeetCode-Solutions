
# coding: utf-8

# # Multiply Strings
# Medium
# 
# Given two non-negative integers num1 and num2 represented as strings, 
# return the product of num1 and num2, also represented as a string.
# 
# Example 1:
# 
# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:
# 
# Input: num1 = "123", num2 = "456"
# Output: "56088"
# Note:
# 
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

# In[33]:


def multiply(num1, num2):
    n1,n2 = 0,0
    for i in num1:
        n1 = n1*10 + ( ord(i) -ord('0'))
    
    for i in  num2:
        n2 = n2*10 + ( ord(i) -ord('0'))
    
    return str(n1*n2)


# In[37]:


J = "3"
S = "4"

print (multiply(J, S))

