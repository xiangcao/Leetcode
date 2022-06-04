# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result=[]
        if not root:
            return result
        queue=[root]
        left_to_right = False
        while queue:
            result.append([node.val for node in queue])
            nextqueue=[]
            while queue:
                node = queue.pop()
                if left_to_right:
                    for next in [node.left, node.right]:
                        if next:
                            nextqueue.append(next)
                else:
                    for next in [node.right, node.left]:
                        if next:
                            nextqueue.append(next)
            left_to_right = not left_to_right
            queue = nextqueue
        return result
            
                
                            
        
