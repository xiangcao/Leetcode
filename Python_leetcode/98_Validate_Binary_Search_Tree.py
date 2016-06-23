# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(root, maxval, minval):
            if not root:
                return True
            if root.val >= maxval or root.val <= minval:
                return False
            return helper(root.left, root.val, minval) and helper(root.right, maxval, root.val)
                
        #return helper(root, sys.maxint, -sys.maxint-1)
        return helper(root, float('inf'), float('-inf'))
            
    def isValidBST(self, root):        
        self.prev = None
        return self.validate(root, self.prev)
    
    def validate(self, node, prev):
        if node == None:
            return True
        if not self.validate(node.left, self.prev):
            return False
        if self.prev != None and self.prev.val >= node.val:
            return False
        self.prev = node
        return self.validate(node.right, self.prev)


