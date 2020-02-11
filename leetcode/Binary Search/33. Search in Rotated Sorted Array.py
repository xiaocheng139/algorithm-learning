#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (33.58%)
# Likes:    3650
# Dislikes: 397
# Total Accepted:    563.8K
# Total Submissions: 1.7M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# 
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# Example 1:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# 
#

# @lc code=start
class Solution:
    #Time Complexity: O(logn)
    #Space Complexity: O(1)
    #Not easy to specify each condition, looking for another approach
    def solution1(self, nums, target):
        if len(nums) == 0:
            return -1

        start = 0
        end = len(nums) -1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid

            if nums[start] > nums[mid]:
                if target < nums[start] and target > nums[mid]:
                    start = mid
                else:
                    end = mid
            else:
                if target >= nums[start] and target <= nums[mid]:
                    end = mid
                else:
                    start = mid

        if nums[start] == target:
            return start

        if nums[end] == target:
            return end
        
        return -1