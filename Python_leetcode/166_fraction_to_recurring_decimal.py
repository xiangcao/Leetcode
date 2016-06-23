#Fraction to Recurring Decimal 
"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

    Given numerator = 1, denominator = 2, return "0.5".
    Given numerator = 2, denominator = 1, return "2".
    Given numerator = 2, denominator = 3, return "0.(6)".

Hint:

    No scary math, just apply elementary math knowledge. Still remember how to perform a long division?
    Try a long division on 4/9, the repeating part is obvious. Now try 4/333. Do you see a pattern?
    Be wary of edge cases! List out as many test cases as you can think of and test your code thoroughly.

"""

# good explanation: https://leetcode.com/discuss/42159/0ms-c-solution-with-detailed-explanations 
# https://leetcode.com/discuss/18731/accepted-cpp-solution-with-explainations 
class Solution(object):
    #"0.(01)"
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        # 66/1000 = 0.066
        # 2/6 = 0.333
        """
         Input: 1 99  PASS
         Input: 1
                90
         Output: "0.01(1)"
         Expected: "0.0(1)" 
         
          Input: 0
                 3
          Output: ""
          Expected: "0" 
        """
        dot = False
        result=[]
        addzero = False
        recurRemainder = []
        recurStart=[]
        negative = False
        if (numerator < 0 and denominator > 0) or  (numerator > 0 and denominator < 0):
            negative = True
        numerator, denominator = abs(numerator), abs(denominator) 
        while numerator:
            time += 1
            quotient = numerator/denominator
            remainder = numerator % denominator
            
            if not quotient:
                if not dot:
                    result.append(".") if result else result.append("0.")
                    dot = True
                if addzero:
                    result.append("0")
                recurRemainder.append(remainder)
                recurStart.append(len(result))
                
                #else:
                    #recurRemainder = remainder
                    #recurStart = len(result)
                numerator = remainder * 10
                addzero = True
            else:
                addzero = False
                
                if recurRemainder and remainder in recurRemainder:
                    recurPosition = recurStart[recurRemainder.index(remainder)]
                    result.insert(recurPosition , "(")
                    result.append(str(quotient)+")")
                    break

                result.append(str(quotient))
                numerator = remainder
        if negative: 
            result.insert(0, '-')
        return ''.join(result) if result else "0"
        
        
    def fractionToDecimal(self, numerator, denominator):
        n, remainder = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator*denominator < 0 else ''
        result = [sign+str(n), '.']
        stack = []
        while remainder not in stack:
            stack.append(remainder)
            n, remainder = divmod(remainder*10, abs(denominator))
            result.append(str(n))
    
        idx = stack.index(remainder)
        result.insert(idx+2, '(')
        result.append(')')
        return ''.join(result).replace('(0)', '').rstrip('.')
                
        
