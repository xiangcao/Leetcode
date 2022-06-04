# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time O(K) in the average case and \mathcal{O}(H + k)O(H+k) in the worst case, where k is an index of closest element
    #Space O(H)
    def closestValue(self, root: TreeNode, target: float) -> int:
        stack, pred = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            if pred < target and target <= root.val:
                return min(pred, root.val, key = lambda x: abs(target - x))
  
            pred = root.val
            root = root.right

        return pred

    #Time complexity : \mathcal{O}(H)O(H) since here one goes from root down to a leaf.
    # space O(1)
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val
        while root:
            closest = min(root.val, closest, key = lambda x: abs(target - x))
            root = root.left if target < root.val else root.right
        return closest
