# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        self.maxsize = 0
        def dfs(root):
            if not root:
                return (0, float("inf"), float("-inf"))
            left_size, left_min, left_max = dfs(root.left)
            right_size, right_min, right_max = dfs(root.right)
            self.maxsize = max(self.maxsize, left_size, right_size)
            if left_size == -1 or right_size == -1 or root.val >= right_min or root.val <= left_max:
                return (-1, float("-inf"), float("inf"))

            return (left_size+right_size+1, min(left_min, root.val), max(right_max, root.val))
        size, smallest, largest = dfs(root)
        return max(self.maxsize, size)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        self.maxsize = 0
        def dfs(root):
            if not root:
                return (0, float("inf"), float("-inf"))
            left_size, left_min, left_max = dfs(root.left)
            right_size, right_min, right_max = dfs(root.right)
            if left_size == -1 or right_size == -1 or root.val >= right_min or root.val <= left_max:
                return (-1, float("-inf"), float("inf"))
            self.maxsize = max(self.maxsize, left_size, right_size, left_size+right_size+1)

            return (left_size+right_size+1, min(left_min, root.val), max(right_max, root.val))
        dfs(root)
        return self.maxsize
