"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        result=[]
        def getPath(path, node):
            if not node:
                return
            if not (node.left or node.right):
                result.append("->".join(path + [str(node.val)]))
                return
            getPath(path + [str(node.val)], node.left)
            getPath(path + [str(node.val)], node.right)
        getPath([], root)
        return result
