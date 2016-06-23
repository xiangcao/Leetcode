# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    #Wrong!!!
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        result = []
        prev = None
        stack.append(root)
        while stack:
            root = stack[-1]
            if root:  # should maintain the invariant "root is never a None" if we add conditions below
                temp = root
                #what if root.left and root.right is both None? 
                
                #left of root is already visited. 
                if root.left == prev:
                    root = root.right  #should add a condition if root.right
                    stack.append(root)
                elif root.right == prev:
                    node = stack.pop()
                    result.append(node.val)
                else:
                    root = root.left   #should add a condition if root.left
                    stack.append(root)
                prev = temp
        
            else:
                stack.pop()
                prev = root
        return result
        
    #accepted
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        result = []
        if not root:
            return result

        prev = -1
        stack.append(root)
        while stack:
            root = stack[-1]
            
            #left of root is already visited.  travesing up from left
            if root.left == prev:
                if root.right:  #should add a condition if root.right
                    stack.append(root.right)
                else:
                    node = stack.pop()
                    result.append(node.val)
            elif root.right == prev:  #right of root is already visited. traversing up from right
                node = stack.pop()
                result.append(node.val)
            else:  # traversing down
                if root.left:   #should add a condition if root.left
                    stack.append(root.left)
                elif root.right:
                    stack.append(root.right)
                else:
                    node = stack.pop()
                    result.append(node.val)
            prev = root
        return result
        
    #Accepted. 
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        result = []
        if not root:
            return result
        prev = -1 #this is only doable in python. what if you can only assign None to prev? (in c++ or java). see below
        stack.append(root)
        while stack:
            root = stack[-1]
            #left of root is not visited
            if root.left and root.left != prev and root.right != prev:
                stack.append(root.left)
            #right of root is not visited (root.left is empty, or root.left == prev)
            elif root.right and root.right != prev:  
                stack.append(root.right)
            else: #root.right is empty or root.right == prev
                node = stack.pop()
                result.append(node.val)
            prev = root

        return result
    #Accepted
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        result = []
        if not root:
            return result
        prev = None
        stack.append(root)
        while stack:
            root = stack[-1]
            #left of root is not visited
            if root.left and ( (root.left != prev and root.right != prev) or not prev):
                stack.append(root.left)
            #right of root is not visited (root.left is empty, or root.left == prev)
            elif root.right and root.right != prev:  
                stack.append(root.right)
            else: #root.right is empty or root.right == prev
                node = stack.pop()
                result.append(node.val)
            prev = root

        return result
               

    #Accepted. 取巧. reverse of a 'pre-order' traversal
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result=[]
        stack=[]
        if not root:
            return result
        stack.append(root)
        while stack:
            root = stack[-1]
            result.append(root.val)
            stack.pop()
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return result[::-1]
 
