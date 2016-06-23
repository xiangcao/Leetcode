class Solution(object):
    #pass
    def isAnagram_(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if ''.join(sorted(s)) == ''.join(sorted(t)):
            return True
        else:
            return False
    #pass
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        count=[0] * 26
        for i in s:
            count[ord(i)-ord('a')] += 1
        for i in t:
            if count[ord(i)-ord('a')] <= 0:
                return False
            count[ord(i)-ord('a')] -= 1
        return True
            
