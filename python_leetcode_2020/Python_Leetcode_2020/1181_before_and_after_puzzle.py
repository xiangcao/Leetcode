"""
Given a list of phrases, generate a list of Before and After puzzles.

A phrase is a string that consists of lowercase English letters and spaces only. No space appears in the start or the end of a phrase. There are no consecutive spaces in a phrase.

Before and After puzzles are phrases that are formed by merging two phrases where the last word of the first phrase is the same as the first word of the second phrase.

Return the Before and After puzzles that can be formed by every two phrases phrases[i] and phrases[j] where i != j. Note that the order of matching two phrases matters, we want to consider both orders.

You should return a list of distinct strings sorted lexicographically.
"""

class Solution(object):
    def beforeAndAfterPuzzles(self, phrases):
        """
        :type phrases: List[str]
        :rtype: List[str]
        """
        first = collections.defaultdict(set)
        last = collections.defaultdict(set)
        res = set()
        for p in phrases:
            strs = p.split(' ')
            if strs[0] in last:
                res |= {a + p[len(strs[0]):] for a in last[strs[0]]}
            if strs[-1] in first:
                res |= {p + b for b in first[strs[-1]]}
            first[strs[0]].add(p[len(strs[0]):])
            last[strs[-1]].add(p)
        return sorted(list(res))
