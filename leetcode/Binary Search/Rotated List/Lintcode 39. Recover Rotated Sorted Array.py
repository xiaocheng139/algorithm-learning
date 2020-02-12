# 39. Recover Rotated Sorted Array

# Given a rotated sorted array, recover it to sorted array in-place.（Ascending）
#
# Example
# Example1:
# [4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5]
# Example2:
# [6,8,9,1,2] -> [1,2,6,8,9]
#
# Challenge
# In-place, O(1) extra space and O(n) time.
#
# Clarification
# What is rotated array?
#
# For example, the orginal array is [1,2,3,4], The rotated array of it can be [1,2,3,4], [2,3,4,1], [3,4,1,2], [4,1,2,3]

class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def solution1(self, nums):
        # Find the lowest number
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[end]:
                start = mid
            else:
                end = mid

        minimum_index = end if nums[start] > nums[end] else start
        if minimum_index == 0:
            return nums
        else:
            return nums[minimum_index:] + nums[:minimum_index]

    # Define a function that reverse the target list
    def reverse(self, nums):
        if len(nums) <= 1:
            return nums

        i, j = 0, len(nums) -1

        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        return nums

solution = Solution()
print(solution.recoverRotatedSortedArray([4,5,1,2,3]))