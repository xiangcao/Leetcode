"""
S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.

Return any permutation of T (as a string) that satisfies this property.
"""

class Solution:
    def customSortString(self, S: str, T: str) -> str:
        ans, cnt = [], collections.Counter(T)           # count each char in T. 
        for c in S:
            if cnt[c]: ans.extend(c * cnt.pop(c))       # sort chars both in T and S by the order of S.
        for c, v in cnt.items():
            ans.extend(c * v)                           # group chars in T but not in S.
        return ''.join(ans);
