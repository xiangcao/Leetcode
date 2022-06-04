"""
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.
"""

# same as 1091_shortest_path_in_binary_matrix

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        q = []
        index = 0
        total_fresh = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 1:
                    total_fresh += 1
                if val == 2:
                    q.append((i, j, 0))
        if total_fresh == 0:
            return 0
        while index < len(q):
            i, j, d = q[index]
            for x, y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    grid[x][y] = 2
                    total_fresh -= 1
                    if total_fresh == 0:
                        return d + 1
                    q.append((x, y, d+1))
            index += 1
        return -1
