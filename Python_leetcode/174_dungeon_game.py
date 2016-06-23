class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n = len(dungeon), len(dungeon[0])
        dp=[0 for i in range(n)]
        dp[-1] = max(1, -dungeon[-1][-1]+1)
        for j in range(n-2, -1, -1):
            dp[j] = max(1,  -dungeon[m-1][j] + dp[j+1])
                    
        for i in range(m-2, -1, -1):
            for j in range(n-1, -1, -1):
                if j == n-1:
                    dp[j] = max(1, -dungeon[i][j] + dp[j])
                else:
                    dp[j] = max(1, -dungeon[i][j] + min(dp[j],dp[j+1]))
                    
        return dp[0]
