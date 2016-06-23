# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        
        while root and root.val <= p.val:
            root = root.right
        
        if not root:
            return None
        
        leftResult = self.inorderSuccessor(root.left, p)
        return leftResult if leftResult else root
            
            
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        succ = None
        while root:
            if root.val > p.val:
                succ = root
                root = root.left
            else:
                root = root.right
        return succ
