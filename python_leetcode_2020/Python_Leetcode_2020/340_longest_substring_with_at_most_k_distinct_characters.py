"""
Given a string, find the length of the longest substring T that contains at most k distinct characters.
"""

class Solution:
    # sliding window
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        count = collections.defaultdict(int)
        start = end = 0
        distinct = 0
        ans = 0
        while end < len(s):
            count[s[end]] += 1
            if count[s[end]] == 1:
                distinct += 1
            end += 1
            while distinct > k:
                count[s[start]] -= 1
                if count[s[start]] == 0:
                    distinct -= 1
                start += 1
            ans = max(ans, end - start)
        return ans
