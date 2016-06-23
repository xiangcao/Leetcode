# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    
    #Accepted 
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        result = []
        
        while root or stack:
            if root:
                result.append(root.val)
                if root.right:     # will work if remove this line. 
                    stack.append(root.right)
                root = root.left
            else:
                root = stack.pop()
        return result
       
    #Accepted 
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        result = []
        if not root:
            return result
        stack.append(root)
        while stack:
            root = stack[-1]
            stack.pop()
            result.append(root.val)
            if root.right:     # will work if remove this line. 
                stack.append(root.right)
            if root.left:
                stack.append(root.left)

        return result
