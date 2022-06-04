"""
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generate_trees(start, end):
            if start > end:
                return [None]
            if start == end:
                return [TreeNode(start)]
            
            all_trees = []
            for i in range(start, end+1):
                ltrees = generate_trees(start, i-1)
                rtrees = generate_trees(i+1, end)
                
                for l in ltrees:
                    for r in rtrees:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        all_trees.append(root)
            return all_trees

        return generate_trees(1, n) if n else []
