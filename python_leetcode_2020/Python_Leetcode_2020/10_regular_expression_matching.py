"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where: 

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).


"""
class Solution(object):
    # Accepted
    def isMatch(self, text, pattern):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])
        
    """
    Intuition

As the problem has an optimal substructure, it is natural to cache intermediate results. We ask the question \text{dp(i, j)}dp(i, j): does \text{text[i:]}text[i:] and \text{pattern[j:]}pattern[j:] match? We can describe our answer in terms of answers to questions involving smaller strings.

Algorithm

We proceed with the same recursion as in Approach 1, except because calls will only ever be made to match(text[i:], pattern[j:]), we use \text{dp(i, j)}dp(i, j) to handle those calls instead, saving us expensive string-building operations and allowing us to cache the intermediate results.

Top-Down Variation
"""
    def isMatch(self, text, pattern):
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)
    """Complexity Analysis

Time Complexity: Let T, PT,P be the lengths of the text and the pattern respectively. The work for every call to dp(i, j) for i=0, ... ,Ti=0,...,T; j=0, ... ,Pj=0,...,P is done once, and it is O(1) work. Hence, the time complexity is O(TP).

Space Complexity: The only memory we use is the O(TP) boolean entries in our cache. Hence, the space complexity is O(TP).
"""
    
    # Bottom up DP
    def isMatch(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]
