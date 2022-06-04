"""
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
"""

class Solution:
    def reorganizeString(self, S: str) -> str:
        n = len(S)
        count = collections.Counter(S)
        letters = sorted(count.keys(), key=lambda x: count[x])
        if count[letters[-1]] > (n+1) // 2:
            return ''
        i = 0
        ans = [''] * n
        while letters:
            l = letters.pop()
            c = count[l]
            while c > 0:
                if i >= n:
                    i = 1
                ans[i] = l
                i += 2
                c -= 1
        return ''.join(ans)
                            
