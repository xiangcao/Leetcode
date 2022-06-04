"""
8. String to Integer (atoi)
Share
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
"""

class Solution:
    def myAtoi(self, str: str) -> int:
        sign = 1
        base = 0
        i = 0
        INT_MAX = (1 << 31) -1 
        INT_MIN = - (1 << 31)
        while i < len(str) and str[i] == ' ':
            i += 1
        if i < len(str) and (str[i] == '-' or str[i] == '+'):
            sign = 1 if str[i] == '+' else -1
            i += 1
        
        while i < len(str) and str[i].isdigit():
            if base > INT_MAX//10 or (base == INT_MAX // 10 and ord(str[i]) - ord('0') > 7):
                return INT_MAX if sign == 1 else INT_MIN
            base = 10 * base + ord(str[i]) - ord('0')
            i += 1
        return base * sign;
        
                
