# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def isSymmetricHelper(left, right):
            if left is None or right is None:
                return left == right
            if left.val != right.val:
                return False
            return isSymmetricHelper(left.right, right.left) and isSymmetricHelper(left.left, right.right)
        return isSymmetricHelper(root.left, root.right)
        
    #iterative solution
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        leftstack, rightstack = [root.left], [root.right]
        
        while leftstack and rightstack:
            left = leftstack.pop()
            right = rightstack.pop()
            if not left and not right:
                continue
            if not left or not right:
                    return False
            if left.val != right.val:
                return False
            leftstack.extend([left.right, left.left])
            rightstack.extend([right.left, right.right])
        return not (leftstack or rightstack)
