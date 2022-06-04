"""
Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = len(t)
        charCount = collections.Counter(t)
        start = end = 0
        window = float("inf")
        ans = 0
        while end < len(s):
            if charCount[s[end]] > 0:
                count -= 1
            # this line is tricky: it must always execute to ensure the line on line 20 works (the line which invokes count += 1)
            charCount[s[end]] -= 1
            end += 1
            while count == 0:
                if (end-start) < window:
                    window = end-start
                    ans = start

                charCount[s[start]] += 1
                if charCount[s[start]] == 1:
                    count += 1
                start += 1
        return "" if window == float('inf') else s[ans:ans+window]
