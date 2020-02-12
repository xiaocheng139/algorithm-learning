#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#
# https://leetcode.com/problems/search-a-2d-matrix-ii/description/
#
# algorithms
# Medium (42.29%)
# Likes:    2364
# Dislikes: 65
# Total Accepted:    259.7K
# Total Submissions: 613.9K
# Testcase Example:  '[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n5'
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
#
#
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
#
#
# Example:
#
# Consider the following matrix:
#
#
# [
# ⁠ [1,   4,  7, 11, 15],
# ⁠ [2,   5,  8, 12, 19],
# ⁠ [3,   6,  9, 16, 22],
# ⁠ [10, 13, 14, 17, 24],
# ⁠ [18, 21, 23, 26, 30]
# ]
#
#
# Given target = 5, return true.
#
# Given target = 20, return false.
#
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not any(matrix):
            return False

        i = len(matrix) - 1
        j = 0

        while i >= 0 and j < len(matrix[0]):
            current_point = matrix[i][j]
            if current_point > target:
                i -= 1
            elif current_point == target:
                return True
            else:
                j += 1

        return False

# @lc code=end

