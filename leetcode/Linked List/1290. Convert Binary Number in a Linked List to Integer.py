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
