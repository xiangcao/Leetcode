"""
 Given a binary tree, flatten it to a linked list in-place.

For example,

If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.flattenRecursive(root)
    def flattenRecursive(self, root):
        if root is None:
            return (None, None)
        root.left, root.right = root.right, root.left
        head1, tail1 = self.flattenRecursive(root.right)
        head2, tail2 = self.flattenRecursive(root.left)
        if tail1 is None:
            root.right = head2
        else:
            tail1.right = head2
        root.left = None
        #candidateTail = [tail2, head2, tail1, head1, root]   #first try. also accepted
        candidateTail = [tail2, tail1, root] 
        tail = None
        for i in candidateTail:
            if i is not None:
                tail =i
                break
        
        return (root, tail)
            
