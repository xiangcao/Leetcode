"""
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.
"""

class Solution:
    #Approach 1: Flood Fill First, we need to remove all land connected to the edges using flood fill.Then, we can count and flood-fill the remaining islands.
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        
        #Flood Fill
        def dfs(i, j):
            if 0<=i<m and 0<=j<n and grid[i][j]==0:
                grid[i][j] = 1
                dfs(i, j+1)
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j-1)
        
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m-1 or j == n-1) and grid[i][j] == 0:
                    dfs(i, j)
                
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dfs(i, j)
                    res += 1
                    
        return res
