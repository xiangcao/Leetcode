"""
In a 2D grid of 0s and 1s, we change at most one 0 to a 1.

After, what is the size of the largest island? (An island is a 4-directionally connected group of 1s).

Example 1:

Input: [[1, 0], [0, 1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
"""
"""
The solution is long, but in fact it is really straight forward.
I suggest not going into my codes but reading my explanations, which should be enough.

Prepare
I have several simple sub function to help me on this kind of problem.

valid(int x, int y), check if (x, y) is valid in the grid.
move(int x, int y), return all possible next position in 4 directions.

Explanation
Only 2 steps:

Explore every island using DFS, count its area, give it an island index and save the result to a {index: area} map.
Loop every cell == 0, check its connected islands and calculate total islands area.

Complexity
Time O(N^2)
Space O(N^2)

"""

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)

        def move(x, y):
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= x + i < N and 0 <= y + j < N:
                    yield x + i, y + j

        def dfs(x, y, index):
            res = 0
            grid[x][y] = index
            for i, j in move(x, y):
                if grid[i][j] == 1:
                    res += dfs(i, j, index)
            return res + 1

        # DFS every island and give it an index of island
        index = 2
        areas = {0: 0}
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 1:
                    areas[index] = dfs(x, y, index)
                    index += 1

        # traverse every 0 cell and count biggest island it can conntect
        res = max(areas.values())
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 0:
                    possible = set(grid[i][j] for i, j in move(x, y))
                    res = max(res, sum(areas[index] for index in possible) + 1)
        return res


# round 2
class Solution:
    # [[1]], output: 1;  (common bug: output 0)
    # [[1,0],[0,1]], output: 3
    def largestIsland(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid)
        index = 2
        mapping = {}
        mapping[0] = 0
        def isvalid(x, y):
            return 0 <= x < M and 0 <= y < N 

        def move(x, y):
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if isvalid(x + dx, y + dy):
                    yield (x+dx, y+dy)

        def fill(x, y, index):
            grid[x][y] = index
            area = 0 
            for nextx, nexty in move(x,y):
                if grid[nextx][nexty] == 1:
                    area += fill(nextx, nexty, index)
            return area + 1

        for x in range(M):
            for y in range(N):
                if grid[x][y] == 1:
                    mapping[index] = fill(x, y, index)
                index += 1

        result = max(mapping.values())
        for x in range(M):
            for y in range(N):
                if grid[x][y] == 0:
                    neighbors = set([grid[nextx][nexty] for nextx, nexty in move(x, y)])
                    result = max(result, sum(mapping[neighbor] for neighbor in neighbors) + 1)
        return result
