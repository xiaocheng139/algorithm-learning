#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (32.77%)
# Likes:    1047
# Dislikes: 1676
# Total Accepted:    472.9K
# Total Submissions: 1.4M
# Testcase Example:  '4'
#
# Implement int sqrt(int x).
# 
# Compute and return the square root of x, where x is guaranteed to be a
# non-negative integer.
# 
# Since the return type is an integer, the decimal digits are truncated and
# only the integer part of the result is returned.
# 
# Example 1:
# 
# 
# Input: 4
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
# the decimal part is truncated, 2 is returned.
# 
# 
#

# @lc code=start
class Solution:
    #Time Complexity: O(logn)
    #Space Complexity: O(1)
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        start = 0
        end = x
        while start + 1 < end:
            mid = start + (end - start) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square > x:
                end = mid
            else:
                start = mid
            
        if x >= end * end:
            return start + 1
        elif x >= start * start:
            return start
        else:
            return start - 1