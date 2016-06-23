"""
 Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
"""

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1,len2 = len(word1),len(word2)
        dp =[[0 for j in range(len2+1)] for i in range(len1+1)]
        for i in range(len1+1):
            dp[i][0] = i
        for j in range(len2+1):
            dp[0][j] = j
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+ (word1[i-1]!=word2[j-1]))
        return dp[len1][len2]
                
        
        
