#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (41.90%)
# Likes:    1197
# Dislikes: 2025
# Total Accepted:    511.7K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty array of digits representing a non-negative integer, plus
# one to the integer.
# 
# The digits are stored such that the most significant digit is at the head of
# the list, and each element in the array contain a single digit.
# 
# You may assume the integer does not contain any leading zero, except the
# number 0 itself.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# 
# 
# Example 2:
# 
# 
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# 
#

# @lc code=start

class Solution:
    def plusOne(self, digits):
        digits.insert(0, 0)
        if digits[-1] == 9:
            to_plus = True
        else:
            digits[-1] += 1
            to_plus = False

        for i in range(len(digits) - 1,  -1, -1):
            if to_plus:
                if digits[i] != 9:
                    digits[i] += 1
                    to_plus = False
                else:
                    digits[i] = 0
                    to_plus = True

        if digits[0] == 0:
            return digits[1::]
        else:
            return digits


solution = Solution()
print(solution.plusOne([8,9,9,9]))