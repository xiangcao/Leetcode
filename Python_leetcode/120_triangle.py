class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = [[0 for i in row] for row in triangle]
        dp[0][0] = triangle[0][0]
        
        for row in range(1, len(triangle)):
            for col in range(len(triangle[row])):
                if col == 0:
                    dp[row][col] = dp[row-1][col] + triangle[row][col]
                elif col == len(triangle[row]) - 1:
                    dp[row][col] = dp[row-1][col-1] + triangle[row][col]
                else:
                    dp[row][col] = min(dp[row-1][col], dp[row-1][col-1]) + triangle[row][col]
        
        return min(dp[-1])
