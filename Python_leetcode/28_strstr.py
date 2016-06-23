class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        source = 0
        targe = 0
        lenOfSource = len(haystack)
        lenOfTarget = len(needle)
        
        while lenOfTarget + source <= lenOfSource:
            target  = 0 
            while target < lenOfTarget:
                if haystack[source+target] != needle[target]:
                    break
                target += 1
            if target == lenOfTarget:
                return source
            source += 1
        return -1
    
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        source = 0 # index interatving over haystack
        target = 0 # index for needle
        if len(needle) == 0:
            return 0
        while source  < len(haystack):
            if target == len(needle):
                break
            if haystack[source] == needle[target]:
                source += 1
                target += 1
            else:
                source = source - target + 1
                target = 0
        
        return source-target if target == len(needle) else -1
        
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        source = 0
        if len(needle) == 0:
            return 0
        while source < len(haystack):
            if haystack[source:len(needle)+source] == needle:
                return source
            else:
                source += 1
        return -1
                
