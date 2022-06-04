# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def dfs(node, presum, curSum):
            if not node:
                return 0
            
            curSum += node.val
            count = presum[curSum-sum]
            presum[curSum] += 1
            
            count += dfs(node.left, presum, curSum) + dfs(node.right, presum, curSum)
            presum[curSum] -= 1
            return count
        presum = collections.defaultdict(int)
        presum[0]  = 1
        return dfs(root, presum, 0)
    
