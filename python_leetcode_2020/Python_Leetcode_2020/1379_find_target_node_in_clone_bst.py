# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def findNode(root):
            if not root:
                return None
            if root.val == target.val:
                return root
            return findNode(root.left) or findNode(root.right)
        return findNode(cloned)
    
    def getTargetCopy2(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def it(node):
            if node:
                yield node
                yield from it(node.left)
                yield from it(node.right)
            
        for n1, n2 in zip(it(original), it(cloned)):
            if n1 == target:
                return n2


    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original or original is target:
            return cloned
        result = self.getTargetCopy(original.left, cloned.left, target)
        if result is not None:
            return result
        return self.getTargetCopy(original.right, cloned.right, target)

