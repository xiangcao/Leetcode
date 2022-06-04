"""
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.
"""

class Solution:
    # time O(n^2), space O(n^2)
    def longestPalindromeSubseq1(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in reversed(range(len(s))):
            dp[i][i] = 1
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        return dp[0][len(s)-1];
    
    # time O(n^2), space O(n)
    # 1304 ms
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [1] * len(s)
        for i in reversed(range(len(s))):
            pre = dp[i]
            for j in range(i+1, len(s)):
                tmp = dp[j]
                if s[i] == s[j]:
                    dp[j] = pre + 2 if i + 1 <= j - 1 else 2
                else:
                    dp[j] = max(dp[j], dp[j-1])
                pre = tmp
        return dp[-1]
        
        
    # 3200 ms
    def longestPalindromeSubseq(self, s: str) -> int:
        def lcs(s1, s2, m, n):
            dp = [[0] * (n+1) for _ in range(m+1)]
            for i in range(m+1):
                for j in range(n+1):
                    if i == 0 or j == 0:
                        continue
                    if s1[i-1] == s2[j-1]:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            return dp[-1][-1]
        return lcs(s, s[::-1], len(s), len(s))
