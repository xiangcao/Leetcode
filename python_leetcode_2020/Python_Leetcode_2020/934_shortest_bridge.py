#Related Question: 827_making_a_large_island.py  
"""
In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)
****************************8****************************8****************************8****************************8****************************8****************************
Intuition

Conceptually, our method is very straightforward: find both islands, then for one of the islands, keep "growing" it by 1 until we touch the second island.

We can use a depth-first search to find the islands, and a breadth-first search to "grow" one of them. This leads to a verbose but correct solution.

Algorithm

To find both islands, look for a square with a 1 we haven't visited, and dfs to get the component of that region. Do this twice. After, we have two components source and target.

To find the shortest bridge, do a BFS from the nodes source. When we reach any node in target, we will have found the shortest distance.

Please see the code for more implementation details.
"""

class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        R, C = len(A), len(A[0])

        def neighbors(r, c):
            for nr, nc in ((r-1,c),(r,c-1),(r+1,c),(r,c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        def get_components():
            done = set()
            components = []
            for r, row in enumerate(A):
                for c, val in enumerate(row):
                    if val  == 1 and (r, c) not in done:
                        # Start dfs
                        stack = [(r, c)]
                        seen = {(r, c)}
                        while stack:
                            node = stack.pop()
                            for nei in neighbors(*node):
                                if A[nei[0]][nei[1]] and nei not in seen:
                                    stack.append(nei)
                                    seen.add(nei)
                        done |= seen
                        components.append(seen)
            return components

        source, target = get_components()
        queue = collections.deque([(node, 0) for node in source])
        done = set(source)
        while queue:
            node, d = queue.popleft()
            if node in target: return d-1
            for nei in neighbors(*node):
                if nei not in done:
                    queue.append((nei, d+1))
                    done.add(nei)


#Optimization: Just need to find one island; then expand from the first islands. whenever we see 1 again, it means we have find the shortest path
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        R, C = len(A), len(A[0])

        def neighbors(r, c):
            for nr, nc in ((r-1,c),(r,c-1),(r+1,c),(r,c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        def get_components():
            done = set()
            components = []
            for r, row in enumerate(A):
                for c, val in enumerate(row):
                    if val and (r, c) not in done:
                        # Start dfs
                        stack = [(r, c)]
                        seen = {(r, c)}
                        while stack:
                            node = stack.pop()
                            for nei in neighbors(*node):
                                if A[nei[0]][nei[1]] and nei not in seen:
                                    stack.append(nei)
                                    seen.add(nei)
                        return seen

        source = get_components()
        queue = collections.deque([(node, 0) for node in source])
        done = source
        while queue:
            node, d = queue.popleft()
            if A[node[0]][node[1]] and d >= 1: return d-1
            for nei in neighbors(*node):
                if nei not in done:
                    queue.append((nei, d+1))
                    done.add(nei)
