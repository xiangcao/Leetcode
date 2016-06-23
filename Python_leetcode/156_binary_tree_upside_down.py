# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if not root.left:
            return root
        newroot = self.upsideDownBinaryTree(root.left)
        rightmost = newroot
        while rightmost.right:
                rightmost = rightmost.right
        rightmost.left = root.right
        rightmost.right = root
        root.right = root.left = None
        return newroot
