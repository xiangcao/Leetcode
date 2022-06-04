# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        result = collections.deque([])
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if len(result) == k:
                if abs(result[0]-target) > abs(root.val-target):
                    result.popleft()
                else:
                    return
            result.append(root.val)
            inorder(root.right)
        inorder(root)
        return result
