"""
Given the root of a binary tree, find the maximum average value of any subtree of that tree.

(A subtree of a tree is any node of that tree plus all its descendants. The average value of a tree is the sum of its values, divided by the number of nodes.)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.avg = float("-inf")
        def calculateSumAndCount(node):
            if not node:
                return 0, 0
            lsum, lcount = calculateSumAndCount(node.left)
            if lcount:
                self.avg = max(self.avg, lsum/lcount)
            rsum, rcount = calculateSumAndCount(node.right)
            if rcount:
                self.avg = max(self.avg, rsum/rcount)
            return lsum+rsum+node.val, lcount+rcount+1
        total, count = calculateSumAndCount(root)
        if count:
            self.avg = max(self.avg, total/count)
        return self.avg
    
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        return self.helper(root)[2]
    
    def helper(self, n: TreeNode) -> List[int]:
        if (n == None): # base case.
            return [0, 0, 0] # sum, count  & average of nodes
        l = self.helper(n.left)
        r = self.helper(n.right) # recurse to children
        sumOfCurTree = l[0] + r[0] + n.val 
        cnt = l[1] + r[1] + 1
        localMax = max(l[2], r[2], sumOfCurTree/cnt)

        return [sumOfCurTree, cnt, localMax]
