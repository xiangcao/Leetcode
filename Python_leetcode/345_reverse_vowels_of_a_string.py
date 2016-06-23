class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(s)
        begin, end = 0, len(l)-1
        def isVowel(s):
            return s.lower() == 'a' or s.lower() == "e" or \
                   s.lower() =="o" or s.lower() == "i" or s.lower() == "u"
        while begin < end:
            while not isVowel(l[begin]) and begin < end:
                begin += 1
            while not isVowel(l[end]) and begin < end:
                end -= 1
            l[begin], l[end] = l[end], l[begin]
            begin += 1
            end -= 1
            
        return ''.join(l)
            
