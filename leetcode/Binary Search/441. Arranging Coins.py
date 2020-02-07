#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#
# https://leetcode.com/problems/arranging-coins/description/
#
# algorithms
# Easy (39.20%)
# Likes:    257
# Dislikes: 553
# Total Accepted:    86.8K
# Total Submissions: 221.3K
# Testcase Example:  '5'
#
# You have a total of n coins that you want to form in a staircase shape, where
# every k-th row must have exactly k coins.
# ⁠
# Given n, find the total number of full staircase rows that can be formed.
# 
# n is a non-negative integer and fits within the range of a 32-bit signed
# integer.
# 
# Example 1:
# 
# n = 5
# 
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤
# 
# Because the 3rd row is incomplete, we return 2.
# 
# 
# 
# Example 2:
# 
# n = 8
# 
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤
# 
# Because the 4th row is incomplete, we return 3.
# 
# 
#

# @lc code=start
class Solution:
    # Time Complexity: O(logn)
    # Space Complexity: O(1)
    # Binary search 
    # Pay attention to dealing with the start and end points
    def solution1(self, n):
        start = 1
        end = n
        while start + 1 < end:
            mid = start + (end - start) // 2
            if mid * (mid + 1) > 2 * n:
                end = mid
            elif mid * (mid + 1) == 2 * n:
                return mid
            else:
                start = mid

        if start * (start + 1) > 2 * n:
            return start - 1
        elif end * (end + 1) > 2 * n:
            return start
        else:
            return end

    #Time Complexity: O(1)
    #Space Complexity: O(1)
    #Not sure sqrt is allowed
    
    def solution2(self, n):
        import math
        # k * (k + 1) <= 2 * n < (k + 1) * (k + 2)
        #So if we get the square root of 2 * n and then do some comparison
        k = int(math.sqrt(2*n))
        if k * (k + 1) > 2 * n:
            return k - 1
        return k