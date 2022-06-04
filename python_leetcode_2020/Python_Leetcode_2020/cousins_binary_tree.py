# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        level = {(root, None)}
        
        def getTuple(left, right):
            if left:
                leftvalue = left.val
            if right:
                rightvalue = right.val
            if leftvalue and rightvalue:
                children = [(left, right)] if leftvalue < rightvalue else [(right, left)]
            else:
                children = [(left, right)]
        target = getTuple(x, y)

        while level:
            nextLevel = {}
            while level:
                left, right = level.pop()
                if left:
                    nextLevel.update(getTuple(left.left, left.right))
                if right:
                    nextLevel.update(getTuple(right.left, right.right))
            if target in nextLevel:
                return True
            level = nextLevel
        return False
        
            
                 
        
        
s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
s.isCousins(root, TreeNode(4), TreeNode(3))

