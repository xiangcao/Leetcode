# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        queue = collections.deque()
        queue.append(root)
        reverse = False
        while queue:
            level = []
            size = len(queue)
            for i in range(size):
                root = queue.popleft()
                level.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            
            if reverse:
                level.reverse()
            result.append(level)
        
            reverse = not reverse
        return result
        
