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
    # Time Complexity: O(logn)
    # Space Complexity: O(n)
    def solution1(self, nums):
        # Find the lowest number
        minimum_index = self.find_minimum_index_type2(nums)
        if minimum_index == 0:
            return nums
        else:
            # This step required extra space
            return nums[minimum_index:] + nums[:minimum_index]

    # Time Complexity: O(logn)
    # Space Complexity: O(n)
    def solution2(self, nums):
        minimum_index = self.find_minimum_index_type2(nums)
        if minimum_index != 0:
            # 3-Step reverse
            self.reverse(nums, 0, minimum_index - 1)
            self.reverse(nums, minimum_index, len(nums) - 1)
            self.reverse(nums, 0, len(nums) - 1)
        return nums

    # Find the lowest number, same as above
    # Attention ! If each element of the array is different
    # Time complexity: O(logn)
    # Space complexity: O(1)
    def find_minimum_index_type1(self, nums):
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[end]:
                start = mid
            else:
                end = mid

        return end if nums[start] > nums[end] else start

    # If there are duplicate numbers in this array, have to traverse all elements
    # Time complexity: O(n)
    # Space complexity: O(1)
    def find_minimum_index_type2(self, nums):
        if not nums:
            return -1

        minimum_index = 0
        for index, val in enumerate(nums):
            if val < nums[minimum_index]:
                minimum_index = index
        return minimum_index

    # Define a function that reverse the target list
    def reverse(self, nums, start, end):
        if len(nums) > 1:
            i, j = start, end
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

solution = Solution()
print(solution.solution2([4,5,6,1,2,3]))