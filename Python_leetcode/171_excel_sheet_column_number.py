"""
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
"""



class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0 
        for i in s:
            sum = sum * 26 + ord(i)-ord('A')+1
        return sum


        return reduce(lambda x, y : x * 26 + y, [ord(c) - 64 for c in list(s)])
# https://leetcode.com/discuss/19725/solutions-languages-does-any-one-have-one-line-solution-java
#   c++ one line:
#   return s != "" ? 26*titleToNumber(s.substr(0,s.size()-1)) + s[s.size()-1] -'A'+1 : 0;

