"""
Given the root of a binary tree, return the number of uni-value subtrees.

A uni-value subtree means all nodes of the subtree have the same value.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        # return a pair (value, count of univalue subtree)
        self.count = 0
        
        def helper(node):
            if not node:
                return True
            left = helper(node.left)
            right = helper(node.right)
            
            if left and right:
                if node.left and node.val != node.left.val:
                    return False
                if node.right and node.val != node.right.val:
                    return False
                
                self.count += 1
                return True
            return False
        helper(root)
        return self.count
        

# leetcode solution
class Solution:
    def countUnivalSubtrees(self, root):
        if root is None: return 0
        self.count = 0
        self.is_uni(root)
        return self.count

    def is_uni(self, node):

        # base case - if the node has no children this is a univalue subtree
        if node.left is None and node.right is None:

            # found a univalue subtree - increment
            self.count += 1
            return True

        is_uni = True

        # check if all of the node's children are univalue subtrees and if they have the same value
        # also recursively call is_uni for children
        if node.left is not None:
            is_uni = self.is_uni(node.left) and is_uni and node.left.val == node.val

        if node.right is not None:
            is_uni = self.is_uni(node.right) and is_uni and node.right.val == node.val

        # increment self.res and return whether a univalue tree exists here
        self.count += is_uni
        return is_uni
