"""
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        columnTable = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])
        mincol, maxcol = 0, 0
        while queue:
            node, col = queue.popleft()
            if node:
                mincol = min(mincol, col)
                maxcol = max(maxcol, col)
                columnTable[col].append(node.val)
                queue.append((node.left, col-1))
                queue.append((node.right, col+1))
        return [columnTable[col] for col in range(mincol, maxcol + 1)]
            
        
            
