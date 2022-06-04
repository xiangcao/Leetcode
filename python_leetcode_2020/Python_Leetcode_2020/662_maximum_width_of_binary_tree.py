# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        queue = collections.deque([])
        queue.append((root, 1))
        maxsize = float("-inf")
        while queue:
            size = len(queue)
            for i in range(size):
                node, index = queue.popleft()
                if i == 0:
                    start = index
                if i == size - 1:
                    end = index
                if node.left:
                    queue.append((node.left, index * 2))
                if node.right:
                    queue.append((node.right, index * 2 + 1))
            maxsize = max(maxsize, end - start + 1) 
        return maxsize
            
