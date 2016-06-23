# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        left = right = root
        ldepth = rdepth = 0
        while left:
            ldepth += 1
            left = left.left
        while right:
            rdepth += 1
            right = right.right
        if ldepth == rdepth:
            return (1 << ldepth) -1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
            
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def getNode(root, path, depth):
            while depth and root:
                depth -= 1
                if path & (1 << depth):
                    root = root.right
                else:
                    root = root.left
                #depth -= 1
            return root
        left = root
        depth = 0
        while left:
            depth += 1
            left = left.left
        if depth == 0 or depth == 1:
            return depth
        print "depth is ", depth
        begin, end = 0, (1 << (depth-1)) - 1
        # find the first empty leaf
        while begin < end:
            mid = begin + (end-begin)/2
            if getNode(root, mid, depth-1):
                begin = mid + 1
            else:
                end = mid
        print "begin is ", begin
        # if there is no empty leaf, begin will be the last non-empty leaf element
        if getNode(root, begin, depth-1):
            return (1 << (depth-1))-1 + begin + 1
        else:
            return (1 << (depth-1))-1 + begin
            
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def getNode(root, path, depth):
            while depth and root:
                depth -= 1
                if path & (1 << depth):
                    root = root.right
                else:
                    root = root.left
                #depth -= 1
            return root
        left = root
        depth = 0
        while left:
            depth += 1
            left = left.left
        if depth == 0 :
            return 0
        print "depth is ", depth
        begin, end = 0, (1 << (depth-1)) - 1
        # find the last non-empty leaf
        while begin < end:
            mid = begin + (end-begin+1)/2
            if getNode(root, mid, depth-1):
                begin = mid
            else:
                end = mid - 1
        return (1 << (depth-1))-1 + begin + 1
