"""
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # top down dfs; store max length as global variable
    def longestConsecutive(self, root: TreeNode) -> int:
        self.maxlen = 0
        def dfs(node, parent, length):
            if not node:
                self.maxlen = max(self.maxlen, length)
                return

            if parent is None or node.val == parent.val + 1:
                length += 1
            else:
                self.maxlen = max(self.maxlen, length)
                length = 1
            dfs(node.left, node, length)
            dfs(node.right, node, length)
        
        dfs(root, None, 0)
        return self.maxlen
    
        def dfs2(node, parent, length):
            if not node:
                return length
            length = length + 1 if (parent and node.val == parent.val + 1) else 1
            return max(length, dfs(node.left, node, length), dfs(node.right, node, length))
        #return dfs(root, None, 0)
                
# bottom up
"""
The bottom-up approach is similar to a post-order traversal. We return the consecutive path length starting at current node to its parent. Then its parent can examine if its node value can be included in this consecutive path.
"""
private int maxLength = 0;
public int longestConsecutive(TreeNode root) {
    dfs(root);
    return maxLength;
}

private int dfs(TreeNode p) {
    if (p == null) return 0;
    int L = dfs(p.left) + 1;
    int R = dfs(p.right) + 1;
    if (p.left != null && p.val + 1 != p.left.val) {
        L = 1;
    }
    if (p.right != null && p.val + 1 != p.right.val) {
        R = 1;
    }
    int length = Math.max(L, R);
    maxLength = Math.max(maxLength, length);
    return length;
}

                
