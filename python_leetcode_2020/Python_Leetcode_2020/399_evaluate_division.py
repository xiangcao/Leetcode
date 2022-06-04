"""
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.


"""

# Build graph and then DFS to find the path between two node
# Other than the above searching operation, we need to handle two exceptional cases as follows:
Case 1): if either of the nodes does not exist in the graph, i.e. the variables did not appear in any of the input equations, then we can assert that no path exists.
Case 2): if the origin and the destination are the same node, we can assume that there exists an invisible self-loop path for each node and the result is one.


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = collections.defaultdict(list)
        for i, equation in enumerate(equations):
            x, y = equation
            graph[x].append((y, values[i]))
            graph[y].append((x, 1.0 / values[i]))
        def findPath(source, target, visited):
            if source not in graph or target not in graph:
                return -1.0
            if source == target:
                return 1.0
            visited.add(source)
            for neighbor, product in graph[source]:
                if neighbor in visited:
                    continue
                if neighbor == target:
                    return product
                nextproduct = findPath(neighbor, target, visited)
                if nextproduct != -1.0:
                    return product * nextproduct
            return -1.0
        return [findPath(source, target, set([])) for source, target in queries]
                
            
            
            

