"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(0, max(self.getMaxLength(root))-1);
        
    def getMaxLength(self, root):
        # return (max length of path ending at root, max length of path that pass through root)
        if not root:
            return 0, 0
        endAtLeft,  passthroughLeft = self.getMaxLength(root.left)
        endAtRight, passthroughRight = self.getMaxLength(root.right)
        return (max(endAtLeft, endAtRight) + 1,  max(passthroughLeft, passthroughRight, endAtLeft + endAtRight +1))


# second round
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.diameter = 0
        def longestPath(child):
            if not child:
                return 0
            left = longestPath(child.left)
            right = longestPath(child.right)
            self.diameter = max(self.diameter, left + right + 1)
            return max(left, right) + 1
        longestPath(root)
        return self.diameter - 1


# third round
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.ans = 0
        self.getMaxLength(root)
        return self.ans
    
    def getMaxLength(self, root):
        if not root:
            return 0
        endAtLeft = self.getMaxLength(root.left)
        endAtRight = self.getMaxLength(root.right)
        self.ans = max(self.ans, endAtLeft + endAtRight)
        return max(endAtLeft, endAtRight) + 1
