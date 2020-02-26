#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (32.67%)
# Likes:    7112
# Dislikes: 1846
# Total Accepted:    1.2M
# Total Submissions: 3.7M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example:
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # Time complexity: O(m+n)
    # Space complexity: O(max(m,n))
    def addTwoNumbers(self, l1, l2):
        sentinel = ListNode(0)
        res = sentinel
        add_one = False
        while l1 or l2:
            total = 0
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
        
            if add_one == True:
                total += 1
           
            if total > 9:
                res.next = ListNode(total%10)
                add_one = True
            else:
                res.next = ListNode(total)
                add_one = False
            res = res.next
        
        if add_one:
            res.next = ListNode(1)
        return sentinel.next
                