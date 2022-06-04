"""
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # Recursive + Memo
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        memo = {}
        def helper(root):
            if not root:
                return 0
            if root in memo:
                return memo[root]
            leftGrandChild = rightGrandChild = 0
            if root.left:
                leftGrandChild = helper(root.left.left) + helper(root.left.right)
            if root.right:
                rightGrandChild = helper(root.right.left) + helper(root.right.right)
 
            notchoose = helper(root.left) + helper(root.right)
            choose = root.val + leftGrandChild + rightGrandChild
            memo[root] = max(notchoose, choose)
            return memo[root]

        return helper(root)
            
            
    # Modify return value of recursive to eliminiate subproblem.
    # avoid repeative computation and no need to store result in a dictionary
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root):
            if not root:
                return 0, 0
            left = helper(root.left)
            right = helper(root.right)
            
            result = [0] * 2
            result[0] = max(left[0], left[1]) + max(right[0], right[1])
            result[1] = root.val + left[0] + right[0]
            return result
        return max(helper(root))
