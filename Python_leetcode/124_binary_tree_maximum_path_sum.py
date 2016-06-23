# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxsum = float("-inf")
        def dfs(root):  # get largest path from children to root 
            if not root:
                return 0
            leftToRoot = max(0, dfs(root.left))  # missing max(0,..) is a common bug in this problem 
            rightToRoot = max(0, dfs(root.right))
            
            self.maxsum = max(self.maxsum, leftToRoot+root.val+rightToRoot)
            return max(leftToRoot, rightToRoot) + root.val
        dfs(root)
        
        return self.maxsum
            
