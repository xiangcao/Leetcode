# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self._leftmost(root)
        
    def _leftmost(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        e = self.stack.pop()
        if e.right:
            self._leftmost(e.right)
        return e.val
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# round 2
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack=[]
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        current = self.stack.pop()
        if current.right:
            root = current.right
            while root:
                self.stack.append(root)
                root = root.left
        return current.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

