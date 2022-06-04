"""
On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 

Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:

Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:

Input: [[0,1],[2,0]]
Output: 0
Explanation: 
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
 

Note:

1 <= grid.length * grid[0].length <= 20
"""

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) 
        
        empty = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start_i, start_j = i, j
                elif grid[i][j] == 2:
                    end_i, end_j = i, j
                elif grid[i][j] == 0:
                    empty += 1
        def neighbor(i, j):
            for nexti, nextj in ((i-1, j), (i, j-1), (i+1, j), (i, j+1)):
                if 0 <= nexti < m and 0 <= nextj < n and grid[nexti][nextj] >= 0 :
                    yield nexti, nextj
        
        self.res = 0
        def dfs(i, j, empty):
            if i == end_i and j == end_j:
                self.res += empty == 0
                return 
            if empty == 0:
                return
            
            grid[i][j] = -1
            for nexti, nextj in neighbor(i, j):
                dfs(nexti, nextj, empty-1)
            grid[i][j] = 0
        dfs(start_i, start_j, empty)
        return self.res
