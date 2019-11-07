
# coding: utf-8

# # Median of Two Sorted Arrays
# Hard
# 
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# 
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# 
# You may assume nums1 and nums2 cannot be both empty.
# 
# Example 1:
# 
# nums1 = [1, 3] nums2 = [2]
# 
# The median is 2.0 Example 2:
# 
# nums1 = [1, 2] nums2 = [3, 4]
# 
# The median is (2 + 3)/2 = 2.5

# In[ ]:


def median(Ar1, Ar2):
    m, n = len(Ar1), len(Ar2)
    if m > n:
        Ar1, Ar2, m, n = Ar2, Ar1, n, m
    if n == 0:
        raise None

    imin, imax, half_len = 0, m, (m + n + 1) / 2
    while imin <= imax:
        i = (imin + imax) / 2
        j = half_len - i
        if i < m and Ar2[j-1] > Ar1[i]:
            # i is small, we need to  increase it
            imin = i + 1
        elif i > 0 and Ar1[i-1] > Ar2[j]:
            # i is  big, we need to decrease it
            imax = i - 1
        else:
            
            
            if i == 0: max_of_left = Ar2[j-1]
            elif j == 0: max_of_left = Ar1[i-1]
            else: max_of_left = max(Ar1[i-1], Ar2[j-1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m: min_of_right = Ar2[j]
            elif j == n: min_of_right = Ar1[i]
            else: min_of_right = min(Ar1[i], Ar2[j])

            return (max_of_left + min_of_right) / 2.0

