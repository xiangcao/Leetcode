# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    min = None
    max = None
    maxsize = 0
    def largestBSTSubtree(self, root):
        
        self._largestBSTSubtree(root)
        return self.maxsize
    def _largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        isBST = True
        leftNodes = self._largestBSTSubtree(root.left)
        curMin = self.min if leftNodes>0 else root.val
        if leftNodes == -1 or (leftNodes and root.val <= self.max): #be careful here. <=
            isBST = False
        rightNodes = self._largestBSTSubtree(root.right)
        curMax = self.max if rightNodes>0 else root.val
        
        if rightNodes == -1 or (rightNodes and root.val >= self.min):
            isBST = False
        if isBST:
            totalNodes = rightNodes + leftNodes + 1
            self.maxsize = max(self.maxsize, totalNodes)
            self.min = curMin
            self.max = curMax
            return totalNodes
        else:
            return -1 
        
        
