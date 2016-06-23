"""
 The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police. 
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            """
            return the maximum money robbed if robbing or not robbing house at the root
            """
            result=[0,0]
            if root is None:
                return result
            left = dfs(root.left)
            right = dfs(root.right)
            #rob 
            result[0] = root.val + left[1] + right[1]
            #not rob
            result[1] = max(left) + max(right)
            return result
        return max(dfs(root))

"""
别人的解法：
http://siukwan.sinaapp.com/?p=1013  
http://codingmelon.com/2016/03/12/house-robber-iii-leetcode-337/
http://www.programcreek.com/2015/03/leetcode-house-robber-iii-java/
http://www.cnblogs.com/Dylan-Java-NYC/p/5324753.html
"""
