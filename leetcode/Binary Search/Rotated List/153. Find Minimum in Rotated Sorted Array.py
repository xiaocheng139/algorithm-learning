#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (44.13%)
# Likes:    1571
# Dislikes: 205
# Total Accepted:    370.8K
# Total Submissions: 840K
# Testcase Example:  '[3,4,5,1,2]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# 
# Find the minimum element.
# 
# You may assume no duplicate exists in the array.
# 
# Example 1:
# 
# 
# Input: [3,4,5,1,2] 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: [4,5,6,7,0,1,2]
# Output: 0
# 
# 
#

# @lc code=start

class Solution:
    # Time Complexity: O(logn)
    # Space Complexity: O(1)
    # Draw a graph to analyse the possible siutations that mid point locates
    
    def findMin(self, nums):
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] <= nums[end]:
                end = mid
            else:
                start = mid
            
        if nums[start] > nums[end]:
            return nums[end]
        else:
            return nums[start]

