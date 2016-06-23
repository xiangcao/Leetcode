class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == []:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for i in range(m)]
        maxSquareSide = 0
        for i in range(m):
            for j in range(n):
                dp[i][j] = int (matrix[i][j])
                if i and j and dp[i][j]:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1 
                maxSquareSide = max(maxSquareSide, dp[i][j])
        return maxSquareSide * maxSquareSide
