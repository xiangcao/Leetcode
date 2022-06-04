# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def helper(root):
            if not root:
                return 0
            if (not (root.left or root.right)):
                self.maxSum = max([self.maxSum,  root.val])
                return root.val
            leftLen = helper(root.left) 
            rightLen = helper(root.right)
            endAtRoot = max(leftLen, rightLen, 0) + root.val
            self.maxSum = max([self.maxSum, endAtRoot, leftLen+rightLen+root.val])
            return endAtRoot
        self.maxSum = float('-inf')
        helper(root)
        return self.maxSum


class Solution(object):
    def maxPathSum(self, root):
        def maxend(node):
            if not node:
                return 0
            left = maxend(node.left)
            right = maxend(node.right)
            self.max = max(self.max, left + node.val + right)
            return max(node.val + max(left, right), 0)
        self.max = None
        maxend(root)
        return self.max

# 2nd round 5 minutes
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxPath = float("-inf")
        def getLongestPath(node):
            if not node:
                return 0
            leftPath = getLongestPath(node.left)
            rightPath = getLongestPath(node.right)
            self.maxPath = max(self.maxPath, leftPath + rightPath + node.val)
            return max(0, max(leftPath, rightPath) + node.val)
        getLongestPath(root)
        return self.maxPath
