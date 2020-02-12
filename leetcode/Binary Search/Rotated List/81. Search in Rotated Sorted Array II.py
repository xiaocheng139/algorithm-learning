#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
#
# algorithms
# Medium (32.90%)
# Likes:    958
# Dislikes: 403
# Total Accepted:    209.1K
# Total Submissions: 635.6K
# Testcase Example:  '[2,5,6,0,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
# 
# You are given a target value to search. If found in the array return true,
# otherwise return false.
# 
# Example 1:
# 
# 
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
# 
# Follow up:
# 
# 
# This is a follow up problem to Search in Rotated Sorted Array, where nums may
# contain duplicates.
# Would this affect the run-time complexity? How and why?
# 
# 
#

# @lc code=start
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    #  Seem like improssible to implement BS, have to traverse 
    def solution1(self, nums, target):
        return target in nums
