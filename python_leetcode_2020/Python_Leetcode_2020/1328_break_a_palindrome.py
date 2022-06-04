"""
Given a palindromic string palindrome, replace exactly one character by any lowercase English letter so that the string becomes the lexicographically smallest possible string that isn't a palindrome.

After doing so, return the final string.  If there is no way to do so, return the empty string.

 

Example 1:

Input: palindrome = "abccba"
Output: "aaccba"
Example 2:

Input: palindrome = "a"
Output: ""
 

Constraints:

1 <= palindrome.length <= 1000
palindrome consists of only lowercase English letters.
"""

class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        if len(palindrome) < 2:
            return ""
        palindrome = list(palindrome)
        for i in range(len(palindrome)/2):
            if palindrome[i] != 'a':
                palindrome[i] = 'a'
                return "".join(palindrome)

        palindrome[-1] = 'b'
        return "".join(palindrome)
