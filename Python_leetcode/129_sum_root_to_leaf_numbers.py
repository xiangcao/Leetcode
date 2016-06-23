# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(sum, root):
            if not root:
                return 0   #this is the key. what to return when root is none. 
            sum = sum * 10 + root.val
            if not root.left and not root.right:
                return sum
            return helper(sum, root.left) + helper(sum, root.right)
         
        return helper(0, root)
