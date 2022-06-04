"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.
"""
#Similar to Leetcode 100 and 101 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time: O(M*N), In worst case (skewed tree), traverse function takes O(M*N) time
    # Space: O(N); The depth of the recursion tree can go up to N is the number of nodes in S
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def isSame(tree1, tree2):
            if not tree1 and not tree2:
                return True
            if not tree1 or not tree2:
                return False
            if tree1.val != tree2.val:
                return False
            return isSame(tree1.left, tree2.left) and isSame(tree1.right, tree2.right)
        return s and (isSame(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t))
        
