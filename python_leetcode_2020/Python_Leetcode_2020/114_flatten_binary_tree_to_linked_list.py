"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    #Same solution as 430 Flatten a multi-level doubly linkedin list
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def flatten(root):
            if not root:
                return None
            lefttail = flatten(root.left)
            righttail = flatten(root.right)
            if lefttail:
                lefttail.right = root.right
                root.right = root.left
                root.left = None
            return righttail or lefttail or root
        flatten(root)
