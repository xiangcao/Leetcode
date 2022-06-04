"""
You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.
"""

class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """
        # first find out root node, which has 0 indegree
        indegree=[0] * n
        for i in range(n):
            if leftChild[i] != -1:
                if indegree[leftChild[i]] == 1:
                    return False
                indegree[leftChild[i]] += 1
            if rightChild[i] != -1:
                if indegree[rightChild[i]] == 1:
                    return False
                indegree[rightChild[i]] += 1
        
        root = -1
        for node, degree in enumerate(indegree):
            if degree == 0:
                root = node
                break
        if root == -1:
            return False
        
        # traverse from root node and verify how many nodes are visited
        def dfs(node):
            if node == -1:
                return 0
            return 1 + dfs(leftChild[node]) + dfs(rightChild[node])
        return dfs(root) == n
