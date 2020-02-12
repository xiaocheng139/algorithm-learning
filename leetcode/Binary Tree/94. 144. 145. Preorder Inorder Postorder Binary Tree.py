#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (60.47%)
# Likes:    2433
# Dislikes: 100
# Total Accepted:    618.2K
# Total Submissions: 1M
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the inorder traversal of its nodes' values.
#
# Example:
#
#
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
#
# Output: [1,3,2]
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
#
#

# @lc code=start
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # Recursive
    def solution1(self, root):
        result = []
        if root:
            self.traverse(root, result)
        return result

    def traverse(self, root, result):
        if root:
            if root.left:
                self.traverse(root.left, result)
            result.append(root.vaule)
            if root.right:
                self.traverse(root.right, result)

    # Iterable
    def solution2(self, root):
        res, stack = [], []
        current_node = root
        while current_node or stack:
            if current_node:
                stack.append(current_node)
                current_node = current_node.left
            else:
                current_node = stack.pop()
                res.append(current_node.val)
                current_node = current_node.right
        return res

    # Divide and Conquer
    def solution3(self, root):
        result = []
        if not root:
            return result

        left = self.solution3(root.left)
        right = self.solution3(root.right)

        result.extend(left)
        result.append(root.val)
        result.extend(right)

        return result


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

exa = Solution()
print(exa.solution3(node1))