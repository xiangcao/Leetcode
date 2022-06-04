"""
Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        first, last = None, None 
        def dfs(node):
            nonlocal last, first
            if not node:
                return
            dfs(node.left)
            if last:
                last.right = node
            elif not first:
                first = node
            node.left = last
            last = node
            dfs(node.right)
        dfs(root)
        if first:
            first.left = last
            last.right = first
        return first

# 2nd round
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        def treeToDList(node):
            leftmin, leftmax, rightmin, rightmax = None, None, None, None
            if node.left:
                leftmin, leftmax = treeToDList(node.left)
                    
                node.left = leftmax
                leftmax.right = node
            if node.right:
                rightmin, rightmax = treeToDList(node.right)
                node.right = rightmin
                rightmin.left = node
            return (leftmin or leftmax or node or rightmin or rightmax ), (rightmax or rightmin or node or leftmax or leftmin)

        first, last = treeToDList(root)
        first.left = last
        last.right = first
        return first
