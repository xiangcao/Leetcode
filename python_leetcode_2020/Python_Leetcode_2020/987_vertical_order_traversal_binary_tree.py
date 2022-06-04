# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = collections.defaultdict(list)
        queue = [(root, 0, 0)]
        minx, max = 0, 0
        while queue:
            nextqueue=[]
            while queue:
                node, x, y = queue.pop()
                minx = min(x, minx)
                maxx = max(x,maxx)
                result[x].append((y,node.val))
                if node.left:
                    nextqueue.append((node.left, x-1, y+1))
                if node.right:
                    nextqueue.append((node.right, x+1, y+1))
            queue = nextqueue
        result_list = []

        for key in range(minx, maxx+1):
            result_list.append(map(lambda x: x[1], sorted(result[key])))
        return result_list 
                
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = collections.defaultdict(list) 
        queue = [(root, 0, 0)]
        while queue:
            nextqueue=[]
            while queue:
                node, x, y = queue.pop()
                result[x].append((y, node.val))
                if node.left:
                    nextqueue.append((node.left, x-1, y+1))
                if node.right:
                    nextqueue.append((node.right, x+1, y+1))
            queue = nextqueue
        orderedKeys = sorted(result.keys())
        result_list = []
        
        for i, key in enumerate(orderedKeys):
            result[key].sort()
            result_list.append(map(lambda x: x[1], result[key]))
        return result_list
                
                
                
             
