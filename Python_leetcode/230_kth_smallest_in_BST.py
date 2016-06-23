# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    #accepted
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def count(root):
            if not root:
                return 0
            return count(root.left) + count(root.right) + 1
        sizeOfLSubtree = count(root.left)
        if sizeOfLSubtree == k-1:
            return root.val
        elif sizeOfLSubtree < k-1:
            return self.kthSmallest(root.right, k-sizeOfLSubtree-1)
        else:
            return self.kthSmallest(root.left, k)
    
    #accepted
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.result = None
        self.n = 0
        def count(root):
            if self.result:
                return
            if not root:
                return
            count(root.left)
            self.n += 1
            if self.n == k:
                self.result = root.val
            count(root.right)
        count(root)
        return self.result
          
    #accepted
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.result = None
        def count(root, n):
            if not root:
                return n
            n = count(root.left, n)
            n += 1
            if n == k:
                self.result = root.val
            n = count(root.right, n)
            return n
            
        count(root, 0)
        return self.result
        
    #Iterative inorder bst traversal
    #accepted
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack=[]
        node = root
        while node:
            stack.append(node)
            node = node.left
        count = 0
        while stack:
            root = stack.pop()
            count += 1
            if count == k:
                return root.val
            right = root.right
            while right:
                stack.append(right)
                right = right.left
        
            
