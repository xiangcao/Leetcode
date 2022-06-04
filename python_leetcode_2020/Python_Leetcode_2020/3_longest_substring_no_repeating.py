class Solution(object):
    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, r = 0, 0
        lookup = set()
        maxLen = 0
        while r < len(s):   
            if s[r] not in lookup:
                lookup.add(s[r])
                maxLen = max(maxLen, r - l + 1)
                r += 1
            else:
                lookup.remove(s[l])
                l += 1
        return maxLen
    
    # Optimized; l directly skip the repeating character index
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, r = 0, 0
        lookup = {}
        maxLen = 0
        while r < len(s):   
            if s[r] in lookup:
                l = max(lookup[s[r]],l)
            maxLen = max(maxLen, r - l + 1)
            lookup[s[r]] = r + 1
            r += 1
        return maxLen
