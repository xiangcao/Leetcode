# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack=[]
        result=[]
        while root:
            stack.append(root)
            root = root.left
        while len(stack):
            root = stack.pop()
            result.append(root.val)
            right = root.right
            while right:
                stack.append(right)
                right = right.left
        return result
            
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack=[]
        result=[]
        if not root:
            return result
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                curnode = stack.pop()
                result.append(curnode.val)
                root = curnode.right
        return result
            
            
            
