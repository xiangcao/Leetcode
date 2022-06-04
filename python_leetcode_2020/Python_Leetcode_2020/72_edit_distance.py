"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
"""

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        dp=[[0] * (n+1) for _ in range(m+1)]
            
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1] + (1 if word1[i-1] != word2[j-1] else 0))
        return dp[m][n]

# 2nd round
    def minDistance(self, word1: str, word2: str) -> int:
        dp=[[0] * (len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(len(word2)):
            dp[0][i+1] = i+1
        for j in range(len(word1)):
            dp[j+1][0] = j+1 
        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j]) + 1
        return dp[-1][-1]
                    
