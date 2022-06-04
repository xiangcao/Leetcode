"""
Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # PostOrder + HashMap Counter
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        self.counter = collections.defaultdict(int)
        self.maxFreq = 0
        def helper(node):
            if not node:
                return 0
            total = helper(node.left) + helper(node.right) + node.val
            self.counter[total] += 1
            self.maxFreq = max(self.maxFreq, self.counter[total])
            return total 
        helper(root)
        return [value for value, freq in self.counter.items() if freq == self.maxFreq]
