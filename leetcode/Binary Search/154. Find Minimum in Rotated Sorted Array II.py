#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
#
# algorithms
# Hard (40.18%)
# Likes:    655
# Dislikes: 185
# Total Accepted:    157.9K
# Total Submissions: 392.7K
# Testcase Example:  '[1,3,5]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# 
# Find the minimum element.
# 
# The array may contain duplicates.
# 
# Example 1:
# 
# 
# Input: [1,3,5]
# Output: 1
# 
# Example 2:
# 
# 
# Input: [2,2,2,0,1]
# Output: 0
# 
# Note:
# 
# 
# This is a follow up problem to Find Minimum in Rotated Sorted Array.
# Would allow duplicates affect the run-time complexity? How and why?
# 
# 
#

# @lc code=start
class Solution:

    # Time Complexity: worst case O(n), average case: O(logn)
    # Space Complexity: O(1)
    # Duplicate elements cause the BS changed, if nums[mid] = nums[end], the last element should be excluded from the scope as there is already an element that is equal to the last element
    # Think about why compare the middle value to the end value instead of the start value -- A special situation is no rotation, so the minimum is located on the start position
    # This will return the fist minimum value (X This is wrong. This will only check the minimum value, for example [1,1,1,1,1,1,1,2,1,1])
    def findMin(self, nums):
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[end]:
                start = mid
            elif nums[mid] < nums[end]:
                end = mid
            else:
                end -= 1
        
        if nums[start] <= nums[end]:
            return nums[start]
        else:
            return nums[end]
