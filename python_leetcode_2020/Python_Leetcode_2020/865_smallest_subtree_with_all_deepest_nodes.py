"""
Given the root of a binary tree, the depth of each node is the shortest distance to the root.

Return the smallest subtree such that it contains all the deepest nodes in the original tree.

A node is called the deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is tree consisting of that node, plus the set of all descendants of that node.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        # return a pair (int depth, TreeNode subtreeWithAllDeepest)
        def helper(root):
            if not root:
                return 0, None
            left_depth, left_ans = helper(root.left)
            right_depth, right_ans = helper(root.right)
            
            if left_depth > right_depth:
                return left_depth + 1, left_ans
            elif left_depth < right_depth:
                return right_depth + 1, right_ans
            else:
                return right_depth + 1, root
        
        return helper(root)[1]
            
            
