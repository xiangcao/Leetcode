# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ''
        leftstr = self.tree2str(t.left)
        rightstr = self.tree2str(t.right)
        if leftstr or rightstr:
            leftstr = '(' + leftstr + ')'
        if rightstr:
            rightstr = '(' + rightstr + ')'
        return str(t.val) + leftstr + rightstr
        
