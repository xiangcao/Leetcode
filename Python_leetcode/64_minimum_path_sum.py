class Solution(object):
    #accepted
    # 2-dimensional dp
    def minPathSum_(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        minPath =[[0 for i in range(n)] for j in range(m)]
        
        minPath[0][0] = grid[0][0]
        
        for j in range(1,n):
            minPath[0][j] = grid[0][j] + minPath[0][j-1]
        for i in range(1, m):
            minPath[i][0] = grid[i][0] + minPath[i-1][0]
        for i in range(1,m):
            for j in range(1,n):
                minPath[i][j] = min(minPath[i-1][j], minPath[i][j-1]) + grid[i][j]
        return minPath[m-1][n-1]
    # one dimensional dp
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        minPath =[0 for i in range(n)]
        
        minPath[0] = grid[0][0]
        
        for j in range(1,n):
            minPath[j] = grid[0][j] + minPath[j-1]
        for i in range(1,m):
            for j in range(0,n):
                if j == 0:
                    minPath[j] = minPath[j] + grid[i][j]
                    continue
                minPath[j] = min(minPath[j], minPath[j-1]) + grid[i][j]
        return minPath[n-1]

        
