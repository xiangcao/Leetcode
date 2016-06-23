"""
113 Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum. 
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def dfs(root, result, path, sum):
            if not root:
                return
            sum -= root.val
            if not sum and not root.left \
                       and not root.right:
                result.append(path+[root.val])
                return
            
            dfs(root.left, result, path+[root.val], sum)
            dfs(root.right, result, path+[root.val], sum)
            
        def dfs(root, result, path, sum):
            if not root:
                return
            sum -= root.val
            if  not root.left and not root.right:
                if sum == 0:
                    result.append(path+[root.val])
            else:
                dfs(root.left, result, path+[root.val], sum)
                dfs(root.right, result, path+[root.val], sum)
            
        result=[]
        path=[]
        dfs(root, result, path, sum)
        return result
                
