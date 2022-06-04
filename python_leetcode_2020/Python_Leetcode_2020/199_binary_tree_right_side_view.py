# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue=collections.deque([root])
        nextqueue=collections.deque([])
        result=[]
        while queue:
            result.append(queue[-1].val)
            while queue:
                node = queue.popleft()
                if node.left:
                    nextqueue.append(node.left)
                if node.right:
                    nextqueue.append(node.right)
            queue = nextqueue
            nextqueue = collections.deque([])
        return result
                

class Solution:
    #DFS
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        rightside = []
        
        def helper(node: TreeNode, level: int) -> None:
            if level == len(rightside):
                rightside.append(node.val)
            for child in [node.right, node.left]:
                if child:
                    helper(child, level + 1)
                
        helper(root, 0)
        return rightside

# 2nd Round BFS
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = collections.deque([root])
        result = []
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i == 0:
                    result.append(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return result
                
                
                
