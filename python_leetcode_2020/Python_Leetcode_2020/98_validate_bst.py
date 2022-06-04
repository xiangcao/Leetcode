"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # test case: [] True
    def isValidBST(self, root: TreeNode) -> bool:
        #preorder (Recursive)
        def dfs(root, left, right):
            if not root:
                return True
            if root.val <= left or root.val >= right:
                return False
            if not dfs(root.left, left, min(right, root.val)):
                return False
            if not dfs(root.right, max(left, root.val), right):
                return False
            return True
        return dfs(root, float("-inf"), float("inf"))
    
    #In-Order, Iterative using stack
    def isValidBST(self, root: TreeNode) -> bool:
        stack, inorder = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True        

   #bottom up
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(root):
            if not root:
                return (True, float("inf"), float("-inf"))
            valid, left_min, left_max = dfs(root.left)
            if not valid or root.val <= left_max:
                return (False, float("-inf"), float("inf"))
            valid, right_min, right_max = dfs(root.right)
            if not valid or root.val >= right_min:
                return (False, float("-inf"), float("inf"))
            return (True, min(left_min, root.val), max(right_max, root.val))
        valid, smallest, largest = dfs(root)
        return valid
