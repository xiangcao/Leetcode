"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,

There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

The total number of unique paths is 2.

Note: m and n will be at most 100.
"""

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        count = [0 for j in range(n)]
        
        for j in range(n):
            if j == 0:
                count[j] = obstacleGrid[0][0] ^ 1
            else:
                count[j] = obstacleGrid[0][j] ^ 1 and count[j-1] ^ 0
        for i in range(1,m):
            for j in range(n):
                if j == 0:
                    count[j] = obstacleGrid[i][0] ^ 1 and count[j] ^ 0
                else:
                    if obstacleGrid[i][j] == 1:
                        count[j] = 0
                    else:    
                        count[j] = count[j-1]  + count[j]
        return count[n-1]
