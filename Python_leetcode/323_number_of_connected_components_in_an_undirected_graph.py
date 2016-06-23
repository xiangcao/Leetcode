#https://leetcode.com/discuss/76907/python-dfs-bfs-union-find-solutions
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        #Union find
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(xy):
            x, y = map(find, xy)
            if x == y:
                return
            if rank[x] < rank[y]:
                parent[x] = y 
            else:
                parent[y]= x 
                if rank[x] == rank[y]:
                    rank[x] += 1
        
        parent, rank = range(n), [0] * n
        
        map(union, edges)
        
        return len({find(x) for x in range(n)})
        
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        #DFS
        visited = [0] * n
        
        graph = [[] for i in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
    
        def dfs(node):
            if not visited[node]:
                visited[node] = 1
                for neighbor in graph[node]:
                    dfs(neighbor)
        
        count = 0 
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1
        return count
        
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        #bfs
        visited = [0] * n
        
        graph = [[] for i in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        count = 0
        for i in range(n):
            if not visited[i]:
                count += 1
                queue = [i]
                for node in queue:
                    if not visited[node]:
                        visited[node] = 1
                        queue += graph[node]
        return count
            
