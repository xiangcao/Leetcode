import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        min_left = left = right  = 0 
        count = collections.Counter(t)
        numCharacter = len(t)
        minWindow = len(s)+1
        while right < len(s):
            #Counter objects return a zero count for missing items. no need to test for existence
            if count[s[right]] > 0:#if s[right] in count and count[s[right]] > 0:
                numCharacter -= 1
            count[s[right]] -= 1
            right += 1
            while numCharacter == 0:
                if right-left < minWindow:
                    minWindow = right - left
                    min_left = left
                
                #if s[left] in count:
                count[s[left]] += 1
                if count[s[left]] > 0:
                    numCharacter += 1

                left += 1
        
        return s[min_left:min_left+minWindow] if minWindow <=len(s) else ""


s = "caddba"
t = "ab"
solution = Solution()
solution.minWindow(s, t)
