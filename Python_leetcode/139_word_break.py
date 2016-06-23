"""
 Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code". 
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        #DP   https://leetcode.com/discuss/18904/java-implementation-using-dp-in-two-ways
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                        dp[i] = True
                        break
        return dp[len(s)]
        
        
    def wordBreak(self, s, words):
        #StefanPochman's solution
        
        ok = [True]
        for i in range(1, len(s)+1):
            ok += any(ok[j] and s[j:i] in words for j in range(i)),
        return ok[-1]
    
    def wordBreak_(self, s, wordDict):
        #BFS
        pass
    
    def wordBreak_(self, s, wordDict):
        #DFS
        pass
