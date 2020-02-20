#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
# https://leetcode.com/problems/implement-strstr/description/
#
# algorithms
# Easy (33.64%)
# Likes:    1276
# Dislikes: 1674
# Total Accepted:    574.9K
# Total Submissions: 1.7M
# Testcase Example:  '"hello"\n"ll"'
#
# Implement strStr().
# 
# Return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
# 
# Example 1:
# 
# 
# Input: haystack = "hello", needle = "ll"
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# 
# 
# Clarification:
# 
# What should we return when needle is an empty string? This is a great
# question to ask during an interview.
# 
# For the purpose of this problem, we will return 0 when needle is an empty
# string. This is consistent to C's strstr() and Java's indexOf().
# 
#

# @lc code=start
class Solution:
    # Time complexity: O(m * n) - Worsr case
    # Space complexity: O(1)
    # This approach is used when slice function is not allowed
    def solution1(self, haystack, needle):
        if len(needle) == 0:
            return 0
        i, j = 0, 0
        while (j < len(needle) and i < len(haystack)):
            if haystack[i] == needle[j]:
                if j == len(needle) - 1:
                    return i - j
                else:
                    i += 1
                    j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    i = i - j + 1
                    j = 0
        return -1

    # Time complexity: O(n) -- Slice complexity is O(m)
    # Space complexity: O(1)
    def solution2(self, haystack, needle):
        if len(needle) == 0:
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1