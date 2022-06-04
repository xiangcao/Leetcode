"""
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Note: The merging process must start from the root nodes of both trees.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not (t1 or t2):
            return None
        
        val1 = t1.val if t1 else 0
        val2 = t2.val if t2 else 0
        newNode = TreeNode(val1+val2)
        t1left = t1.left if t1 else None
        t2left = t2.left if t2 else None
        t1right = t1.right if t1 else None
        t2right = t2.right if t2 else None
        newNode.left = self.mergeTrees(t1left, t2left)
        newNode.right = self.mergeTrees(t1right, t2right)
        return newNode
    
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if (t1 == null)
            return t2;
        if (t2 == null)
            return t1;
        t1.val += t2.val;
        t1.left = mergeTrees(t1.left, t2.left);
        t1.right = mergeTrees(t1.right, t2.right);
        return t1;
