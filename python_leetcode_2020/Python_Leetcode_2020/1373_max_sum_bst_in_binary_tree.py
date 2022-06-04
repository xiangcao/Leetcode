"""
Given a binary tree root, the task is to return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # similar to 98: Validate Binary Search 
    def maxSumBST(self, root: TreeNode) -> int:
        self.maxsum = 0
        def postOrder(root: TreeNode) -> List[int]:
            if not root:
                return [float("inf"), float("-inf"), 0]
            left = postOrder(root.left)
            right = postOrder(root.right)
            
            if (not (left and right and root.val > left[1] and root.val < right[0])):
                return None
            cursum = root.val + left[2] + right[2]
            self.maxsum = max(self.maxsum, cursum)
            return (min(root.val, left[0]), max(root.val, right[1]), cursum)
        postOrder(root)
        return self.maxsum
