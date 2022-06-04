"""
Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split its set of nodes into two independent subsets A and B, such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

Constraints:

1 <= graph.length <= 100
0 <= graphp[i].length < 100
0 <= graph[i][j] <= graph.length - 1
graph[i][j] != i
All the values of graph[i] are unique.
The graph is guaranteed to be undirected. 
"""
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = 0
        colorMap = {}
        def dfs(node, color):
            if node in colorMap:
                return colorMap[node] == color
            colorMap[node] = color
            for child in graph[node]:
                if not dfs(child, 1-color):
                    return False
            return True
 
        for i in range(len(graph)):
            if i in colorMap:
                continue
            if not dfs(i, color):
                return False
        return True
