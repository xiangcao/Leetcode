"""
Given a set of keywords words and a string S, make all appearances of all keywords in S bold. Any letters between <b> and </b> tags become bold.

The returned string should use the least number of tags possible, and of course the tags should form a valid combination.

For example, given that words = ["ab", "bc"] and S = "aabcd", we should return "a<b>abc</b>d". Note that returning "a<b>a<b>b</b>c</b>d" would use more tags, so it is incorrect.

Constraints:

words has length in range [0, 50].
words[i] has length in range [1, 10].
S has length in range [0, 500].
All characters in words[i] and S are lowercase letters.
Note: This question is the same as 616: https://leetcode.com/problems/add-bold-tag-in-string/
"""

class Solution:
    # N is length of S; 
    # Time complexity O(N*Sum(wi))
    # Space complexity O(N)
    def boldWords1(self, words: List[str], S: str) -> str:
        N = len(S)
        mask = [False] * N
        for i in range(N):
            prefix = S[i:]
            for word in words:
                if prefix.startswith(word):
                    for j in range(i, i+len(word)):
                        mask[j] = True
        
        ans = []
        i = 0
        while i < len(S):
            while i < len(S) and mask[i] == False:
                ans.append(S[i])
                i += 1
            if i < len(S):
                ans.append('<b>')
                while i < len(S) and mask[i] == True:
                    ans.append(S[i])
                    i += 1
                ans.append('</b>')
        return "".join(ans)

        """for incl, grp in itertools.groupby(zip(S, mask), lambda z: z[1]):
            if incl: ans.append("<b>")
            ans.append("".join(z[0] for z in grp))
            if incl: ans.append("</b>")
        return "".join(ans) 
        """
# round 2; 
#slightly different implementation in the second loop.  had to add additonal statement after the loop ended
    """
    "abcde" ["abc", "cde"] ==> <b>abcde</b>
    "abcxyz" ["abc", "xyz"]  ==> <b>abcxyz</b>
    """
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        mask = [False] * len(s)
        for i in range(len(s)):
            substr = s[i:]
            for word in dict:
                if substr.startswith(word):
                    for j in range(i, i+len(word)):
                        mask[j] = True

        result = []
        inblock = False
        for i in range(len(s)):
            if not mask[i]:
                if inblock:
                    result.append('</b>'+s[i])
                    inblock = False
                else:
                    result.append(s[i])
            else:
                if inblock:
                    result.append(s[i])
                else:
                    result.append('<b>'+s[i])
                    inblock = True
        if inblock:
            result.append('</b>')
        return "".join(result)
    
    """optimized python solution using trie tree and merge intervals:

        trie tree is used to speed up string match (faster than find or startwith in large query request).
        Using merge intervals instead of mask to reduce Time and Space Complexity, both from O(n) to O(m), m represets interval numbers after merged.
    """
        
    def boldWords(self, words: 'List[str]', S: str) -> str:
        trie, n, intervals, res = {}, len(S), [], ""
        # create trie tree
        for w in words:
            cur = trie
            for c in w:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur["#"] = 0

        # interval merge
        def add_interval(interval):
            if intervals and intervals[-1][1] >= interval[0]:
                if intervals[-1][1] < interval[1]:
                    intervals[-1][1] = interval[1]
            else:
                intervals.append(interval)

        # make max match and add to interval
        for i in range(n):
            cur, j, max_end = trie, i, None
            for j in range(i, n):
                if S[j] not in cur:
                    break
                cur = cur[S[j]]
                if "#" in cur:
                    max_end = j + 1
            # just need to add max-match interval
            if max_end:
                add_interval([i, max_end])

        # concat result
        res, prev_end = "", 0
        for start, end in intervals:
            res += S[prev_end:start] + '<b>' + S[start:end] + "</b>"
            prev_end = end
        return res + S[prev_end:]
