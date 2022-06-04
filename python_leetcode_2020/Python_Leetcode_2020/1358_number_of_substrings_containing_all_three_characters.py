"""
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

Constraints:

3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.
"""
class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = i = 0
        count = {c: 0 for c in 'abc'}
        for j in xrange(len(s)):
            count[s[j]] += 1
            while all(count.values()):
                count[s[i]] -= 1
                i += 1
            res += i
        return res
