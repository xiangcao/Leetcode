"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
"""

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        result = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    result += 4
                    if c != 0:
                        result -= 2 * grid[r][c-1]

                    if r != 0:
                        result -= 2 * grid[r-1][c]

        return result
                

# solution 1
loop over the matrix and count the number of islands;
if the current dot is an island, count if it has any right neighbour or down neighbour;
the result is islands * 4 - neighbours * 2
public class Solution {
    public int islandPerimeter(int[][] grid) {
        int islands = 0, neighbours = 0;

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == 1) {
                    islands++; // count islands
                    if (i < grid.length - 1 && grid[i + 1][j] == 1) neighbours++; // count down neighbours
                    if (j < grid[i].length - 1 && grid[i][j + 1] == 1) neighbours++; // count right neighbours
                }
            }
        }

        return islands * 4 - neighbours * 2;
    }
}

# solution 2  The idea is each time, we encounter a boundary, count++;
# iterative:
class Solution {
    public int islandPerimeter(int[][] grid) {
      int m = grid.length, n = grid[0].length;
      int count = 0;
      int[][] dir = {{0,1},{1,0},{-1,0},{0,-1}};
      for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
          if(grid[i][j] == 1){
            for(int[] d:  dir){
              int x = i + d[0], y = j + d[1];
              if(x < 0 || y < 0 || x == m || y == n || grid[x][y] == 0){
                count++;
              }
            } 
          }
        }
      }
      return count;  
    }
}
#recursive
class Solution {
    public int islandPerimeter(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        for(int i = 0; i<m; i++){
            for(int j = 0; j<n; j++){
                if(grid[i][j]==1){
                    return dfs(grid, i,j);
                }
            }
        }
        
        return 0;
    }
    public int dfs(int[][] grid, int i, int j){
        if(i<0 ||i>=grid.length|| j<0 || j>=grid[0].length||grid[i][j]==0) return 1;
        if(grid[i][j]==-1) return 0;
        int res = 0;
        grid[i][j] = -1;
        res += dfs(grid, i+1, j)+dfs(grid, i-1, j)+dfs(grid, i, j+1)+dfs(grid,i,j-1);
        
        return res;
    }
}
python version
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def dfs(grid, i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 1
            if grid[i][j] == -1:
                return 0
            grid[i][j] = -1
            return dfs(grid, i-1, j) + dfs(grid, i+1, j) + dfs(grid, i, j+1) + dfs(grid, i, j-1)
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return dfs(grid, i, j)
        return 0
    
        
