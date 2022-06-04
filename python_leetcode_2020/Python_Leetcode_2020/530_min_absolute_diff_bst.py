# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.prev = None
        self.mindiff = float('inf')
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if self.prev is not None:
                self.mindiff = min(self.mindiff, root.val - self.prev)
            self.prev = root.val
            dfs(root.right)
        dfs(root)
        return self.mindiff
    
    def getMinimumDifference2(self, root):
        L = []
        def dfs(node):
            if node.left: dfs(node.left)
            L.append(node.val)
            if node.right: dfs(node.right)
        dfs(root)
        return min(b - a for a, b in zip(L, L[1:]))


    # don't use global minimum; don't do in-order traversal

    def getMinimumDifference(self, root: TreeNode) -> int:
        def fn(node, lo, hi):
            if not node: return hi - lo
            left = fn(node.left, lo, node.val)
            right = fn(node.right, node.val, hi)
            return min(left, right)
        return fn(root, float('-inf'), float('inf'))

    def getMinimumDifference(self, root: TreeNode) -> int:
        def mindiff(root, lo, hi):
            if not root:
                return float('inf')
            return min(root.val - lo,
                       hi - root.val,
                       mindiff(root.left, lo, root.val),
                       mindiff(root.right, root.val, hi))
        return mindiff(root, float('-inf'), float('inf'))
