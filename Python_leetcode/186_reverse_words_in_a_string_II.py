 """
Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces and the words are always separated by a single space.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Could you do it in-place without allocating extra space?

Related problem: Rotate Array
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        self.reverse(s, 0, len(s)-1)
        begin = 0
        for i in range(len(s)):
            if s[i] == ' ':
                self.reverse(s, begin, i-1)
                begin = i+1
        self.reverse(s, begin, len(s)-1)
        
    def reverse(self, s, begin, end):
        while begin < end:
            s[begin], s[end] = s[end], s[begin]
            begin += 1
            end -= 1
            
        
