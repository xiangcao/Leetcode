"""
Given a string s, return the maximum number of ocurrences of any substring under the following rules:

The number of unique characters in the substring must be less than or equal to maxLetters.
The substring size must be between minSize and maxSize inclusive.
 
"""

class Solution(object):
    # sliding window
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        start = result = 0 
        count = collections.defaultdict(int)
        
        occurence = collections.defaultdict(int)
        
        for i in range(len(s)):
            count[s[i]] += 1
            if i - start + 1 > minSize:
                count[s[start]] -= 1
                if count[s[start]] == 0:
                    count.pop(s[start])
                start += 1
            
            if i - start + 1 == minSize and len(count) <= maxLetters:
                substring = s[start:i+1]
                occurence[substring] += 1
                result = max(result, occurence[substring])
        return result
                
        
