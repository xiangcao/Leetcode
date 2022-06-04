"""
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Note: This question is the same as 538: https://leetcode.com/problems/convert-bst-to-greater-tree/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # pass totalSum as function parameter
    def bstToGst1(self, root: TreeNode) -> TreeNode:
        def helper(root, totalSum):
            if not root:
                return totalSum
            totalSum = helper(root.right, totalSum)
            totalSum = root.val = root.val + totalSum
            return helper(root.left, totalSum)
            
        helper(root, 0)
        return root
        
    # use class variable
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        def helper(root):
            if not root:
                return
            helper(root.right)
            self.sum = root.val = root.val + self.sum
            helper(root.left)
            
        helper(root)
        return root
