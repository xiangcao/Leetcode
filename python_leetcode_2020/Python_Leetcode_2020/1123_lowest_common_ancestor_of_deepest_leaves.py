"""
Given a rooted binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

The node of a binary tree is a leaf if and only if it has no children
The depth of the root of the tree is 0, and if the depth of a node is d, the depth of each of its children is d+1.
The lowest common ancestor of a set S of nodes is the node A with the largest depth such that every node in S is in the subtree with root A.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    Complexity
    Both solution are one pass.
    Time O(N) for one pass
    Space O(H) for recursion management

    Solution 1: Get Subtree Height and LCA
    helper function return the subtree height and lca and at the same time.
    null node will return depth 0,
    leaves will return depth 1.

    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def getLCAAndHeight(root):
            if not root:
                return 0, root
            
            left_h, left_lca = getLCAAndHeight(root.left)
            right_h, right_lca = getLCAAndHeight(root.right)
            if left_h > right_h:
                return left_h+1, left_lca
            elif left_h < right_h:
                return right_h+1, right_lca
            else:
                return left_h+1, root
        return getLCAAndHeight(root)[1]
        
