# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = collections.defaultdict(list)
        def dfs(root):
            if not root:
                return -1
            leftdepth = dfs(root.left)
            rightdepth = dfs(root.right)
            curdepth = max(rightdepth, leftdepth) + 1 # must add 1 here. 
            result[curdepth].append(root.val)
            return curdepth
        maxdepth = dfs(root)
        return [result[i] for i in range(maxdepth+1)]
            
