# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.post_index = len(postorder)-1
        self.index_map = {val: idx for idx, val in enumerate(inorder)}
        def helper(left=0, right=len(postorder)):
            if left == right:
                return None
            root = TreeNode(postorder[self.post_index])
            index = self.index_map[root.val]
            self.post_index -= 1
            root.right = helper(index+1, right)
            root.left = helper(left, index)
            return root
        return helper()
        
            
            
            
