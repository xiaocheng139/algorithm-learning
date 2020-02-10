#
# @lc app=leetcode id=1290 lang=python3
#
# [1290] Convert Binary Number in a Linked List to Integer
#
# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/
#
# algorithms
# Easy (80.24%)
# Likes:    172
# Dislikes: 19
# Total Accepted:    27.9K
# Total Submissions: 34.8K
# Testcase Example:  '[1,0,1]'
#
# Given head which is a reference node to a singly-linked list. The value of
# each node in the linked list is either 0 or 1. The linked list holds the
# binary representation of a number.
# 
# Return the decimal value of the number in the linked list.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10
# 
# 
# Example 2:
# 
# 
# Input: head = [0]
# Output: 0
# 
# 
# Example 3:
# 
# 
# Input: head = [1]
# Output: 1
# 
# 
# Example 4:
# 
# 
# Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
# Output: 18880
# 
# 
# Example 5:
# 
# 
# Input: head = [0,0]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# The Linked List is not empty.
# Number of nodes will not exceed 30.
# Each node's value is either 0 or 1.
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def solution1(self, head):
        current_node = head
        arr = []

        while current_node:
            arr.append(current_node.val)
            current_node = current_node.next

        #Now we have a list of binary numbers, convert it to decimal
        return int(''.join([str(ele) for ele in arr]), 2)


    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def solution2(self, head):
        current_node = head
        binary_str = ''

        while current_node:
            binary_str += str(current_node.val)
            current_node = current_node.next

        return int(binary_str, 2)
