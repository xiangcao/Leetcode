"""We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        parents = {}
        def dfs(node, parent):
            if not node:
                return
            parents[node] = parent
            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root, None)
        
        queue = collections.deque([(target, 0)])
        seen = {target}
        while queue:
            node, dist = queue.popleft()
            if dist == K:
                return [node.val] + [x.val for x, dist in queue]
        
            for nei in (node.left, node.right, parents[node]):
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, dist+1))
        return []
