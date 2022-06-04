"""
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples 1:

Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7 

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
 """

BFS, put node, col into queue at the same time
Every left child access col - 1 while right child col + 1
This maps node into different col buckets
Get col boundary min and max on the fly
Retrieve result from cols
"""
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result=[]
        queue = collections.deque([])
        queue.append((root, 0))
        mincol, maxcol = 0, 0
        mapping = collections.defaultdict(list)
        while queue:
            node, col = queue.popleft()
            mapping[col].append(node.val)
            mincol = min(mincol, col)
            maxcol = max(maxcol, col)
            if node.left:
                queue.append((node.left, col-1))
            if node.right:
                queue.append((node.right, col+1))
        
        for col in range(mincol, maxcol + 1):
            result.append(mapping[col])
        return result
