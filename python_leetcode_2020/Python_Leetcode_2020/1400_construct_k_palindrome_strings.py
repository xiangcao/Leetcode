"""
Given a string s and an integer k. You should construct k non-empty palindrome strings using all the characters in s.

Return True if you can use all the characters in s to construct k palindrome strings or False otherwise.

Constraints:

1 <= s.length <= 10^5
All characters in s are lower-case English letters.
1 <= k <= 10^5
 
"""
class Solution(object):
    """
    If we have more odd frequency characters than palindromes, then at least 2 odd frequency characters must be in the same palindrome. Since this is not possible, we return true if we have fewer or equal to k odd frequency characters.
    """
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        if len(s) < k:
            return False
        # a string can be palindrome if the number of odd character is 1 or 0
        # for k palindrome, we need 0<= t <= k odd character. 
        odd = sum(1 for c, count in collections.Counter(s).items() if count %2 == 1)
        return odd <= k
