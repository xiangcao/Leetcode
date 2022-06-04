"""
Given a binary search tree, return a balanced binary search tree with the same node values.

A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.

If there is more than one answer, return any of them.

Constraints:

The number of nodes in the tree is between 1 and 10^4.
The tree nodes will have distinct values between 1 and 10^5.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # convert bst to ordered list
        def convertToList(root):
            if not root:
                return None, None
            leftHead, leftTail = convertToList(root.left)
            if leftTail:
                leftTail.right = root
            rightH, rightT = convertToList(root.right)
            root.right = rightH
            return leftHead or root, rightT or root
        head, tail = convertToList(root)
        return self.sortedListToBST(head)

    # time : O(N)
    # space O(LogN)
    def sortedListToBST(self, head: TreeNode) -> TreeNode:
        p = head
        self.head = head
        n = 0
        while p:
            p = p.right
            n += 1
        def convert(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            left = convert(l, mid-1)
            root = self.head
            self.head = self.head.right
            root.left = left
            root.right = convert(mid+1, r)
            return root
        return convert(0, n-1)
