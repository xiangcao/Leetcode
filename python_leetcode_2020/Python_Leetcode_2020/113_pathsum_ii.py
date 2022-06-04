"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.pathList = []
        def dfs(node, path, remainingSum):
            if not node:
                return
            path.append(node.val)
            if not (node.left or node.right) and node.val ==remainingSum:
                self.pathList.append(list(path))
            else:
                dfs(node.left, path, remainingSum-node.val)
                dfs(node.right, path, remainingSum-node.val)
            path.pop()
        dfs(root, [], sum)
        return self.pathList
