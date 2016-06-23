# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return sys.maxint

        child = root.left if root.val > target else root.right
        closest  = self.closestValue(child, target)
        return closest if abs(closest-target) < abs(root.val-target) else root.val
            
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        child = root.left if root.val > target else root.right
        if child:
            closest  = self.closestValue(child, target)
        else:
            return root.val
        return closest if abs(closest-target) < abs(root.val-target) else root.val
    
    #iterative solution
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        closest = root.val
        while root:
            if abs(root.val-target) < abs(closest-target):
                closest = root.val
            if target < root.val:
                root = root.left
            else:
                root = root.right
        return closest
            
