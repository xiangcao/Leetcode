# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    firstMisplaced = secondMisplaced = None
    import sys
    lastVisited = TreeNode(-sys.maxint-1)
    
    #Wrong. 
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.recoverTree(root.left)
        if self.lastVisited > root.val:
            if not self.firstMisplaced:
                self.firstMisplaced = root
            else:
                self.secondMisplaced = root
        self.lastVisited = root.val
        self.recoverTree(root.right)
         
        #think about it. the code below will be executed multile times.
        if self.firstMisplaced and self.secondMisplaced:
            self.firstMisplaced.val, self.secondMisplaced.val = self.secondMisplaced.val, self.firstMisplaced.val
        
    #Accepted
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self._recoverTree(root)
        
        if self.firstMisplaced and self.secondMisplaced:
            self.firstMisplaced.val, self.secondMisplaced.val = self.secondMisplaced.val, self.firstMisplaced.val
            
    def _recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self._recoverTree(root.left)
        if self.lastVisited.val > root.val and not self.firstMisplaced:
                self.firstMisplaced = self.lastVisited
          
        if self.lastVisited.val > root.val and self.firstMisplaced:
            self.secondMisplaced = root

        self.lastVisited = root
        self._recoverTree(root.right)
        
        


sol = Solution()
node= TreeNode(2)
node.right = TreeNode(1)
sol.recoverTree(root)
