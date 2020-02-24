#
# @lc app=leetcode id=925 lang=python3
#
# [925] Long Pressed Name
#
# https://leetcode.com/problems/long-pressed-name/description/
#
# algorithms
# Easy (44.65%)
# Likes:    409
# Dislikes: 53
# Total Accepted:    30.1K
# Total Submissions: 67.2K
# Testcase Example:  '"alex"\n"aaleex"'
#
# Your friend is typing his name into a keyboard.  Sometimes, when typing a
# character c, the key might get long pressed, and the character will be typed
# 1 or more times.
# 
# You examine the typed characters of the keyboard.  Return True if it is
# possible that it was your friends name, with some characters (possibly none)
# being long pressed.
# 
# 
# 
# Example 1:
# 
# 
# Input: name = "alex", typed = "aaleex"
# Output: true
# Explanation: 'a' and 'e' in 'alex' were long pressed.
# 
# 
# 
# Example 2:
# 
# 
# Input: name = "saeed", typed = "ssaaedd"
# Output: false
# Explanation: 'e' must have been pressed twice, but it wasn't in the typed
# output.
# 
# 
# 
# Example 3:
# 
# 
# Input: name = "leelee", typed = "lleeelee"
# Output: true
# 
# 
# 
# Example 4:
# 
# 
# Input: name = "laiden", typed = "laiden"
# Output: true
# Explanation: It's not necessary to long press any character.
# 
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# name.length <= 1000
# typed.length <= 1000
# The characters of name and typed are lowercase letters.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    # Time complexity: O(m + n)
    # Space complexity: O(1)
    # Came accross this problem before, need to specify the 3 situations
    def isLongPressedName(self, name, typed):
        i, j = 0, 0
        prev = None
        
        while i < len(name) or j < len(typed):
            # Can combine the 3 situations into 2
            if i >= len(name):
                if typed[j] == prev:
                    prev = typed[j]
                    j += 1
            elif j >= len(typed):
                return False
            else:
                if name[i] == typed[j]:
                    prev = typed[j]
                    i += 1
                    j += 1
                else:
                    if typed[j] == prev:
                        prev = typed[j]
                        j += 1
                    else:
                        return False

        return True