# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        node1 = node2 = None
        if root == p or root == q:
            return root
        node1 = self.lowestCommonAncestor(root.left,p, q)
        node2 = self.lowestCommonAncestor(root.right, p, q)
        if node1 and node2:
            return root
        return node1 if node1 else node2
