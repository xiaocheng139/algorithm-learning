#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (35.79%)
# Likes:    1283
# Dislikes: 138
# Total Accepted:    282.8K
# Total Submissions: 789.5K
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,50]]\n3'
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
#
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the
# previous row.
#
#
# Example 1:
#
#
# Input:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 3
# Output: true
#
#
# Example 2:
#
#
# Input:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 13
# Output: false
#
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target):
        if not any(matrix):
            return False

        # BS by Column
        start = 0
        end = len(matrix) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if matrix[mid][0] < target:
                start = mid
            elif matrix[mid][0] == target:
                return True
            else:
                end = mid

        # BS by row
        target_row = matrix[start] if target < matrix[end][0] else matrix[end]

        start_2 = 0
        end_2 = len(target_row) - 1
        while start_2 + 1 < end_2:
            mid_2 = start_2 + (end_2 - start_2) // 2
            if target_row[mid_2] < target:
                start_2 = mid_2
            elif target_row[mid_2] == target:
                return True
            else:
                end_2 = mid_2

        if target_row[start_2] == target or target_row[end_2] == target:
            return True
        return False