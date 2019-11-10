
# coding: utf-8

# # Word Search
# Medium
# 
# Given a 2D board and a word, find if the word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
# 
# Example:
# 
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# 
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.

# In[53]:


def findChr(board, strng):
    for x in strng:
        a = str(board).find(x)
        if a <= 0:
            print(False)
            break
        else:
            continue
        return True


# In[54]:


b = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

sr = 'ABM'


# In[52]:


print(findChr(b, sr))

