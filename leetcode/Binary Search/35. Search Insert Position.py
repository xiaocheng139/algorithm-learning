#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position/description/
#
# algorithms
# Easy (41.41%)
# Likes:    1782
# Dislikes: 214
# Total Accepted:    512.8K
# Total Submissions: 1.2M
# Testcase Example:  '[1,3,5,6]\n5'
#
# Given a sorted array and a target value, return the index if the target is
# found. If not, return the index where it would be if it were inserted in
# order.
# 
# You may assume no duplicates in the array.
# 
# Example 1:
# 
# 
# Input: [1,3,5,6], 5
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [1,3,5,6], 2
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: [1,3,5,6], 7
# Output: 4
# 
# 
# Example 4:
# 
# 
# Input: [1,3,5,6], 0
# Output: 0
# 
# 
#

# @lc code=start
class Solution:
    #Time Complexity: O(logn)
    #Space Complexity O(1)
    def searchInsert(self, nums, target):
        if not nums:
            return 0
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            selected_ele = nums[mid]

            if selected_ele > target:
                end = mid
            elif selected_ele == target:
                return mid
            else:
                start = mid
        
        if target <= nums[start]:
            return start
        elif target <= nums[end]:
            return end
        else:
            return end + 1
        