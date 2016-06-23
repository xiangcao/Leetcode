# Given a binary tree, return all root-to-leaf paths. 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []
        
        if not root.left and not root.right:
            return [str(root.val)]

        leftPathToLeaf = self.binaryTreePaths(root.left) 
        rightPathToLeaf = self.binaryTreePaths(root.right)
        
        left = [str(root.val)+ ("->"+lpath ) for lpath in leftPathToLeaf]
        right = [str(root.val)+ ("->"+rpath) for rpath in rightPathToLeaf]
        return left+right
