class Solution:
    # DP
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        result = None
        dp = [[True] * n for _ in range(n)]
    
        for j in range(n):
            for i in range(j, -1, -1):
                dp[i][j] = s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1])

                if (dp[i][j] and (result is None or j - i + 1 > len(result))):
                    result = s[i:j+1]
        return result

    def longestPalindrome2(self, s: str) -> str:
        if len(s) < 2: 
            return s
        
        def extendAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
                
        start, end = 0, 0
        for i in range(len(s)):
            leftLen = extendAroundCenter(i, i)
            rightLen = extendAroundCenter(i, i+1)
            length = max(leftLen, rightLen)
            if (length > (end-start)):
                start = i - (length-1) // 2
                end = i + length//2
        return s[start:end+1]
            
            
