#132. Palindrome Partitioning II
"""
 Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut. 
"""
"""
https://leetcode.com/discuss/53981/56-ms-python-with-explanation
The main algorithm idea is if s[i,j] is a palindrome, then the minCut(s[:j]) is at most minCut(s[:i-1])+1.
This literally needs to find out all possible palindromes in the list. The above post provides an efficient search algorithm. O(n) space and O(n^2) time complexity.

https://leetcode.com/discuss/47140/two-versions-given-one-28ms-one-manancher-like-algorithm-10 
When we construct isPalin array, we update minCuts everytime we found a palindrome sub-string, i.e. if s[i..j] is a palindrome, then minCuts[j+1] will be updated to the minimum of the current minCuts[j+1] and minCut[i]+1(i.e. cut s[0..j] into s[0,i-1] and s[i,j]). At last, we return minCuts[N]. So the complexity is O(N^2).


https://leetcode.com/discuss/43950/python-100ms-extra-dealing-super-cases-reduces-576ms-100ms
https://leetcode.com/discuss/9476/solution-does-not-need-table-palindrome-right-uses-only-space

"""

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        dp = [[0 if j-i <  else j-i for j in range(len(s))] for i in range(len(s))]
        
        for length in range(2,len(s)+1):
            for i in range(len(s)-length+1):
                if dp[i+1][i+length-2] == 0 and s[i] == s[i+length-1]:
                    dp[i][i+length-1] = 0 
                else:
                    dp[i][i+length-1] = min(dp[i+1][i+length-1], dp[i][i+length-2]) + 1
        return dp[0][len(s)-1]
        """
        lens = len(s)
        isPalindrom = [[False] * (i+1) for i in range(lens)]
        dp = range(lens) + [-1]  # to deal with the case j=0, dp[j-1] means dp[-1]
        for i in range(lens):
            for j in range(i, -1, -1):
                if s[j] == s[i] and (i-j <= 2 or isPalindrom[i-1][j+1]):
                    isPalindrom[i][j] = True
                    dp[i] = min(dp[i], dp[j-1]+1)
        return dp[lens-1]
