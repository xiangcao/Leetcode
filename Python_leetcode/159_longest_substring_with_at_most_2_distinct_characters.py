class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 0
        start = 0 
        table=collections.defaultdict(int)
        #eceeeeb
        for i in range(len(s)):
            table[s[i]] += 1
            while len(table) >2:
                if table[s[start]] > 1:
                    table[s[start]] -= 1
                else:
                    table.pop(s[start])
                start += 1
            maxLen = max(maxLen, i - start + 1)
        return maxLen
            
#louise's solution!

class Solution(Object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
           return len(s)

        j = -1
        start = ans = 0

        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                if j >= 0 and s[i] != s[j]:
                    start = j + 1
                j = i - 1
            ans = max(ans, i - start + 1)
        return ans


