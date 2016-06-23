class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        maxLen = 0
        start = 0 
        table=collections.defaultdict(int)
        #eceeeeb
        for i in range(len(s)):
            table[s[i]] += 1
            while len(table) >k:
                if table[s[start]] > 1:
                    table[s[start]] -= 1
                else:
                    table.pop(s[start])
                start += 1
            maxLen = max(maxLen, i - start + 1)
        return maxLen
