"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]

"""
class Solution:
    # Backtracking
    def partition1(self, s: str) -> List[List[str]]:
        results = []
        def isPalindrom(s, start, end):
            while start <= end and s[start] == s[end]:
                start += 1
                end -= 1
            return start > end

        def dfs(s, start, currentPath, result):
            if start >= len(s):
                results.append(currentPath)
                return
            for end in range(start, len(s)):
                if(isPalindrom(s, start, end)):
                    dfs(s, end+1, currentPath + [s[start:end+1]], result)
        dfs(s, 0, [], results)
        return results
    
    # Backtracking + DP. dp is used to check if substring is palindrome
    def partition(self, s: str) -> List[List[str]]:
        results = []
        dp= [[False] * len(s) for _ in range(len(s))]
        def isPalindrom(s, start, end):
            if s[end] == s[start] and (end-start<=2 or dp[start+1][end-1]):
                dp[start][end] = True
                return dp[start][end]
        def dfs(s, start, currentPath, results):
            if start >= len(s):
                results.append(currentPath)
                return
            for end in range(start, len(s)):
                if(isPalindrom(s, start, end)):
                    dfs(s, end+1, currentPath + [s[start:end+1]], results)
        dfs(s, 0, [], results)
        return results
            
            
            
            
            
            
            
            
        
        
                    
        
