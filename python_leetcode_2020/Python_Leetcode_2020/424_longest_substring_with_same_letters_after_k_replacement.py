"""
Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104
"""

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = collections.Counter()
        left = 0
        maxcount = 0
        n = len(s)
        for i in range(n):
            count[s[i]] += 1
            maxcount = max(maxcount, count[s[i]])
            if i - left + 1 - maxcount > k:
                count[s[left]] -= 1
                left += 1
        return n - left

