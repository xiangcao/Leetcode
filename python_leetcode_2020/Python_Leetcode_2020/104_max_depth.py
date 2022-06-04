# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None: 
            return 0 
        else: 
            left_height = self.maxDepth(root.left) 
            right_height = self.maxDepth(root.right) 
            return max(left_height, right_height) + 1

# BFS
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
	Deque<TreeNode> dq = new ArrayDeque<>();
        int depth = 0, next = 0;
        TreeNode cur;
        dq.offer(root);
        
        while (!dq.isEmpty()) {
            depth++;
            next = dq.size();
            for (int i = 0; i < next; ++i) {
                cur = dq.poll();
                if (cur.left != null) dq.offer(cur.left);
                if (cur.right != null) dq.offer(cur.right);
            }
        }
        return depth;
    }
}
