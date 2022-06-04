# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Resursive
    def postorderTraversal1(self, root: TreeNode) -> List[int]:
        result=[]
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            result.append(root.val)
        dfs(root)
        return result

    # Iterative with stack; Pre-order (right child first) then reverse
    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1]
    
    # Iterative stack post-order
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack, result=[], []
        while stack or root:
            while root:
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                root = root.left
            root = stack.pop()
            if stack and root.right == stack[-1]:
                stack[-1] = root
                root = root.right
            else:
                result.append(root.val)
                root = None
        return result
                
        
