class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX, INT_MIN = 2147483647,  -2147483648
        if abs(dividend) < abs(divisor):
            return 0
        neg = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0 )
        remain, divisorAbs = abs(dividend), abs(divisor)
        result = 0 
        
        while remain >= divisorAbs:  #buggy solution: while remain > divisorAbs:  (when dividend=1, divisor=1)
            sum = divisorAbs
            count = 1
            
            while sum + sum < remain:
                sum += sum
                count += count
            remain -= sum
            if result > INT_MAX-count: 
                return INT_MIN if neg else INT_MAX
            result += count
        
        
        return 0-result if neg else result
        
            
        
        
