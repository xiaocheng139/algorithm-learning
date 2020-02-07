#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
#
# algorithms
# Easy (52.46%)
# Likes:    1282
# Dislikes: 514
# Total Accepted:    339.2K
# Total Submissions: 646.4K
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers that is already sorted in ascending order, find
# two numbers such that they add up to a specific target number.
# 
# The function twoSum should return indices of the two numbers such that they
# add up to the target, where index1 must be less than index2.
# 
# Note:
# 
# 
# Your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution and you may
# not use the same element twice.
# 
# 
# Example:
# 
# 
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
# 
#

# @lc code=start
class Solution:
    # Time complexity: O(logn)
    # Space complexity: O(1)
    # Two pointers
    def twoSum(self, numbers, target):
        if len(numbers) < 2:
            return []
        start, end = 0, len(numbers) - 1
        while start < end:
            total = numbers[start] + numbers[end]
            if total == target:
                return [start + 1, end + 1]
            elif total < target:
                start += 1
            else:
                end -= 1
        return []