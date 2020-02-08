Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # Time complexity: O(n)
    # Space Complexity: O(n)
    # Traverse all nodes on the linked list and save them to a list, then retrieve the mid element
    def solution1(self, head):
        current_node = head
        arr = []
        while current_node:
            arr.append(current_node)
            current_node = current_node.next

        return arr[len(arr) // 2]

    # Time complexity: O(n)
    # Space Complexity: O(1)
    # (Get from forum) Set two nodes traverse from the head, the one is one time faster than the other, when the faster node goes to the end, the slow node will go to the middle
    def solution2(self, head):
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

