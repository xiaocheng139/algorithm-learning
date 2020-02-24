#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (51.04%)
# Likes:    3261
# Dislikes: 485
# Total Accepted:    825.8K
# Total Submissions: 1.6M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
# 
# Example:
# 
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
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
    # Time complexitly: O(m + n)
    # Space complexity: O(m + n ) -- Create nodes and connect them 
    def my_solution(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val > l2.val:
            current_node = ListNode(l2.val)
            l2 = l2.next
        else:
            current_node = ListNode(l1.val)
            l1 = l1.next

        res = current_node

        while l1 or l2:
            if l1 and l2:
                if l1.val > l2.val:
                    current_node.next = ListNode(l2.val)
                    l2 = l2.next
                else:
                    current_node.next = ListNode(l1.val)
                    l1 = l1.next
            elif l1:
                current_node.next = ListNode(l1.val)
                l1 = l1.next
            else:
                current_node.next = ListNode(l2.val)
                l2 = l2.next
            current_node = current_node.next

        return res


    # Time complexity: O(m + n)
    # Space complexity: O(1) -- Connect existing nodes
    # This approach create an new node at the first place and link it to the existing nodes 
    def ref_solution(self, l1: ListNode, l2: ListNode) -> ListNode:
        pointer = ListNode(0)
        res = pointer
        while l1 and l2:
            if l1.val > l2.val:
               pointer.next = l2
               l2 = l2.next
            else:
                pointer.next = l1
                l1 = l1.next
            pointer = pointer.next
        # if one of the linked list have not been traversed, link the rest to the pointer
        if l1:
            pointer.next = l1
        if l2:
            pointer.next = l2
        return res.next
        