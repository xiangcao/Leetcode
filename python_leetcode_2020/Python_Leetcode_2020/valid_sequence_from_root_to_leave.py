"""
Given a binary tree where each path going from the root to any leaf form a valid sequence, check if a given string is a valid sequence in such binary tree. 

We get the given string from the concatenation of an array of integers arr and the concatenation of all values of the nodes along a path results in a sequence in the given binary tree.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidSequence(self, root, arr):
        """
        :type root: TreeNode
        :type arr: List[int]
        :rtype: bool
        """
        if not root:
            return False
        return self.helper(root, arr, 0)
    def helper(self, root, arr, curpos):
        if not root:
            return False;
        if curpos >= len(arr):
            return False
        if root.val != arr[curpos]:
            return False
        if root.left or root.right:
            return self.helper(root.left, arr, curpos+1) or self.helper(root.right, arr, curpos+1)
        else:
            return curpos == len(arr)-1

        
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        
        def dfs(node: TreeNode, depth: int) -> bool:
            if node is None or depth >= len(arr) or arr[depth] != node.val:
                return False
            if node.left == node.right == None: # credit to @The_Legend_ for making the code clean
                return depth + 1 == len(arr)
            return dfs(node.left, depth + 1) or dfs(node.right, depth + 1)

        return dfs(root, 0)
