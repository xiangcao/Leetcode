class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        
        #dfs
        matrix = [[] for i in range(n)]
        for edge in edges:
            matrix[edge[0]].append(edge[1])
            matrix[edge[1]].append(edge[0])
        
        visited = [0] * n
        def dfs(node):
            for nbr in matrix[node]:
                if not visited[nbr]:
                    visited[nbr] = 1
                    matrix[nbr].remove(node)
                    if not dfs(nbr):
                        return False
                else:
                    return False
            return True
        count  = 0 
        for node in range(n):
            if not visited[node]:
                if count:
                    return False
                visited[node] = 1
                if not dfs(node):
                    return False
                count += 1
        return True
        
        #bfs
        
        #union find
            
