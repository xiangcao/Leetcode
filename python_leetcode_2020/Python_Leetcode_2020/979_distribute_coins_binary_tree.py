# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.answer = 0
        def dfs(root):
            if not root:
                return 0
            left_balance = dfs(root.left)
            right_balance = dfs(root.right)
            self.answer += abs(left_balance) + abs(right_balance)
            return left_balance + right_balance + root.val - 1
        dfs(root)
        return self.answer
        
