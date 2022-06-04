"""

Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:

Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].
 

Example 2:

Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
 

Note: All the values of tree nodes are in the range of [-1e7, 1e7].
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxval = 0
    def longestConsecutive(self, root: TreeNode) -> int:
        self.longestPath(root);
        return self.maxval;
    def longestPath(self, root: TreeNode) -> List[int]:
        if not root:
            return [0, 0]
        inr = dcr = 1
        if root.left:
            l = self.longestPath(root.left)
            if root.val == root.left.val + 1:
                dcr = l[1] + 1
            elif root.val == root.left.val - 1:
                inr = l[0] + 1
        if root.right:
            r = self.longestPath(root.right)
            if (root.val == root.right.val + 1):
                dcr = max(dcr, r[1] + 1)
            elif (root.val == root.right.val - 1):
                inr = max(inr, r[0] + 1)
        self.maxval = max(self.maxval, dcr + inr - 1);
        return [inr, dcr]


    #Similar solution; slightly different code
    def longestConsecutive(self, root: TreeNode) -> int:
        def longest_path(root):
            if not root:
                return 0, 0
            inc, dec = 1, 1
            l_inc, l_dec = longest_path(root.left)
            r_inc, r_dec = longest_path(root.right)
            if root.left:
                if root.left.val == root.val + 1:
                    inc = max(inc, 1 + l_inc)
                if root.left.val == root.val - 1:
                    dec = max(dec, 1 + l_dec)
            if root.right:
                if root.right.val == root.val + 1:
                    inc = max(inc, 1 + r_inc)
                if root.right.val == root.val - 1:
                    dec = max(dec, 1 + r_dec)
            res[0] = max(res[0], inc + dec - 1)
            return (inc, dec)
        
        res = [0]
        longest_path(root)
        return res[0]
