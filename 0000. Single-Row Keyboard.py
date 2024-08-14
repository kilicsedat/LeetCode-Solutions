
# coding: utf-8

# # single row keyboard
# There is a special keyboard with all keys in a single row.
# 
# Given a string keyboard of length 26 indicating the layout of the keyboard (indexed from 0 to 25), 
# initially your finger is at index 0.
# To type a character, you have to move your finger to the index of the desired character. 
# The time taken to move your finger from index i to index j is |i – j|.
# 
# You want to type a string word. Write a function to calculate how much time it takes to type it with one finger.
# 
# Example 1:
# 
# Input: keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"
# Output: 4
# Explanation: The index moves from 0 to 2 to write 'c' then to 1 to write 'b' then to 0 again to write 'a'.
# Total time = 2 + 1 + 1 = 4. 

# In[1]:


def singlerowkyeb(strng):
    keyboard = "abcdefghijklmnopqrstuvwxyz"
    c = 0
    d = 0
    for i in range (len(string)):
        if i == 0:
            d = abs(keyboard.index(strng[i]))
        else:
            d = abs(keyboard.index(strng[i]) - keyboard.index(strng[i-1]))
        c = c + d
    return c


# In[5]:


print(singlerowkyeb('ffpo'))

