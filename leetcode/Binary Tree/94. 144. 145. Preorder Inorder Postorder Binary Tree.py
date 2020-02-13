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


class Recursive:
    # Recursive
    def in_order(self, root):
        result = []
        if root:
            self.in_order_traverse(root, result)
        return result

    def in_order_traverse(self, root, result):
        if root:
            if root.left:
                self.in_order_traverse(root.left, result)
            result.append(root.vaule)
            if root.right:
                self.in_order_traverse(root.right, result)

# This approach is smart but not sure the space usage is the same as the regular iterative approach
# TODO check the space usage of this approach
class Iterative:
    # Time complexity: O(n)
    # Space Complexity: O(n)
    def in_order(self, root):
        result, stack = [], [root]
        while stack:
            current_ele = stack.pop()
            if current_ele:
                if isinstance(current_ele, TreeNode):
                    stack.append(current_ele.right)
                    stack.append(current_ele.val)
                    stack.append(current_ele.left)
                else:
                    result.append(current_ele)
        return result

    def pre_order(self, root):
        result, stack = [], [root]
        while stack:
            current_ele = stack.pop()
            if current_ele:
                if isinstance(current_ele, TreeNode):
                    stack.append(current_ele.right)
                    stack.append(current_ele.left)
                    stack.append(current_ele.val)
                else:
                    result.append(current_ele)
        return result


    def post_order(self, root):
        result, stack = [], [root]
        while stack:
            current_ele = stack.pop()
            if current_ele:
                if isinstance(current_ele, TreeNode):
                    stack.append(current_ele.val)
                    stack.append(current_ele.right)
                    stack.append(current_ele.left)
                else:
                    result.append(current_ele)
        return result


class DQ:
    def post_order(self, root):
        result = []
        if not root:
            return result

        left = self.post_order(root.left)
        right = self.post_order(root.right)

        result.extend(left)
        result.extend(right)
        result.append(root.val)

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
#    1
#  2   3
# 4 5 6 7

# 4 5 2 6 7 3 1
exa = Iterative()
print(exa.post_order(node1))
print(exa.in_order(node1))
print(exa.pre_order(node1))

# test = DQ()
# print(test.post_order(node1))