# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#http://www.cnblogs.com/yrbbest/p/5065457.html
#https://leetcode.com/discuss/75054/5ms-java-clean-solution

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #get max depth of tree
        if not root:
            return []
        def maxdepth(root):
            if not root:
                return 0
            return 1 + max(maxdepth(root.left), maxdepth(root.right))
        depth = maxdepth(root)
        #max col
        maxcol = (depth-1)*2+1
        result = [[] for i in range(maxcol)]
        
        def preorder(root, col, level):
            if not root:
                return
            
            result[col].append((root.val, level))
            preorder(root.left, col-1, level+1)
            preorder(root.right, col+1, level+1)

        preorder(root, depth-1, 0)

        result = [sorted(col, key=lambda x:x[1]) for col in result if col ]
        result = [ [position[0] for position in col] for col in result ]
        return result
