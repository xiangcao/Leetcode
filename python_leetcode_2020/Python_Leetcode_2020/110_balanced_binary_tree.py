"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def dfs(node):
            if not node:
                return 0
            if not(node.left or node.right):
                return 1
            
            leftheight = dfs(node.left)
            rightheight = dfs(node.right)
            if leftheight < 0 or rightheight < 0:
                return -1
            if abs(leftheight - rightheight) <= 1:
                return max(leftheight, rightheight) + 1
            else:
                return -1
            
        return dfs(root) != -1
        
