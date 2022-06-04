"""
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.

"""
class Solution(object):
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False

        adj_list = [[] for _ in range(n)]
        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)

        seen = set()

        def dfs(node, parent):
            if node in seen: return False;
            seen.add(node)
            for neighbour in adj_list[node]:
                if neighbour == parent:
                    continue
                if not dfs(neighbour, node): return False
            return True

        # We return true iff no cycles were detected,
        # AND the entire graph has been reached.
        return dfs(0, -1) and len(seen) == n
"""
Depending on how much graph theory you know, there's a better definition for determining whether or not a given graph is a tree.

For the graph to be a valid tree, it must have exactly n - 1 edges. Any less, and it can't possibly be fully connected. Any more, and it has to contain cycles. Additionally, if the graph is fully connected and contains exactly n - 1 edges, it can't possibly contain a cycle, and therefore must be a tree!

Going by this definition, our algorithm needs to do the following:

Check whether or not there are n - 1 edges. If there's not, then return false.
Check whether or not the graph is fully connected. Return true if it is, false if otherwise.

    
    # don't need to check if there is a cycle or not. 
    def validTree(self, n, edges):
        if len(edges) != n - 1: return False

        # Create an adjacency list.
        adj_list = [[] for _ in range(n)]
        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)

        # We still need a seen set to prevent our code from infinite
        # looping if there *is* cycles (and on the trivial cycles!)
        seen = set()

        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            for neighbour in adj_list[node]:
                dfs(neighbour)

        dfs(0)
        return len(seen) == n
