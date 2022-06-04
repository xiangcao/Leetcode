"""
Given a string s and an integer k, find out if the given string is a K-Palindrome or not.

A string is K-Palindrome if it can be transformed into a palindrome by removing at most k characters from it.
"""

# Intuition: Find the longest Palindrom and check if its length is >= len(s)-k
class Solution:
    # Optimize 2dimension Dp into 1 dimension DP
    def isValidPalindrome(self, s: str, k: int) -> bool:
        def longestPalindromeSubseq(s: str) -> int:
            dp = [1] * len(s)
            for i in reversed(range(len(s))):
                pre = None
                for j in range(i+1, len(s)):
                    tmp = dp[j]
                    if s[i] == s[j]:
                        dp[j] = pre + 2 if i + 1 <= j - 1 else 2
                    else:
                        dp[j] = max(dp[j], dp[j-1])
                    pre = tmp
            return dp[-1]
        return longestPalindromeSubseq(s) >= (len(s)-k)

Find the length of the longest palindromic subsequence, then plus k to check if the sum reaches the length of the original input string.
Refer to 516. Longest Palindromic Subsequence, and new2500's graph is very helpful.

dp[i][j]: the longest palindromic subsequence's length of substring(i, j), where i, j are left, right indices of the string.
State transition:
if s.charAt(i) == s.charAt(j):
dp[i][j] = dp[i+1][j-1] + 2
otherwise,
dp[i][j] = Math.max(dp[i+1][j], dp[i][j-1]).
dp[i][i] Initialized to 1.

    public boolean isValidPalindrome(String s, int k) {
        int[][] dp = new int[s.length()][s.length()];
        for (int i = s.length() - 1; i >= 0; i--) {
            dp[i][i] = 1;
            for (int j = i + 1; j < s.length(); ++j) {
                if (s.charAt(i) == s.charAt(j)) { dp[i][j] = dp[i + 1][j - 1] + 2; } 
                else { dp[i][j] = Math.max(dp[i + 1][j], dp[i][j - 1]); }
            }
        }
        return s.length() <= k + dp[0][s.length() - 1];
    }
/////////////////////////////////////////////////////////    Longest common substring of the given string & its reverse will be the longest palindromic sequence.


The idea is to find the longest palindromic subsequence(lps) of the given string.
|lps - original string| <= k,
then the string is k-palindrome.

Eg:

One of the lps of string pqrstrp is prsrp.
Characters not contributing to lps of the
string should be removed in order to make the string palindrome. So on removing q and s (or t) from pqrstrp,
string will transform into a palindrome.

public boolean isValidPalindrome(String str, int k) {
        int n = str.length();

        StringBuilder stringBuilder = new StringBuilder(str).reverse();
        int lps = lcs(str, stringBuilder.toString(), n, n);

        return (n - lps <= k);
    }

    /*
    longest palindromic subsequence:
    LCS of the given string & its reverse will be the longest palindromic sequence.
     */
    private int lcs(String X, String Y, int m, int n) {
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                if (i == 0 || j == 0) {
                    dp[i][j] = 0;
                } else if (X.charAt(i - 1) == Y.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp[m][n];
    }
