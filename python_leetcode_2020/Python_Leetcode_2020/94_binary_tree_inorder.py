# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal1(self, root: TreeNode) -> List[int]:
        result = []
        def dfs(root):
            if not root:return
            dfs(root.left)
            result.append(root.val)
            dfs(root.right)
        dfs(root)
        return result
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result=[]
        stack=[]
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.val)
            node = node.right
        return result
            
        
