"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

Constraints:

-231 <= numerator, denominator <= 231 - 1
denominator != 0

"""

#Detail style problem
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        """
        1/4 = 0.25
        1/2 = 0.5
        """
        if numerator == 0:
            return "0"
        result=[]
        if (numerator < 0) ^ (denominator < 0):
            result.append('-')
        numerator = abs(numerator)
        denominator = abs(denominator)
        result.append(str(numerator//denominator))
        remainder = numerator % denominator
        if remainder == 0:
            return "".join(result)
        
        result.append(".")

        remainderMap={}
        while remainder != 0:
            if remainder in remainderMap:
                result.insert(remainderMap[remainder], '(')
                result.append(')')
                return "".join(result)
            remainderMap[remainder] = len(result)
            remainder *= 10
            result.append(str(remainder//denominator))
            remainder = remainder % denominator
        return "".join(result)
                
        



