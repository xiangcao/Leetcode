class Solution:
    """
    2147483647
     1
     Time Limit Exceeded
    """
    #FAIL
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2147483647        # 2**31 - 1
        MIN_INT = -2147483648       # -2**31

        # Special case: overflow.
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        quotient = 0
        negative = False
        if divisor < 0:
            divisor *= -1
            negative = not negative
        if dividend < 0:
            dividend *= -1
            negative = not negative
        multiplier = 1
        while dividend >= divisor:
            if dividend >= divisor * multiplier:
                dividend -= divisor * multiplier
                quotient += 1 * multiplier
                multiplier << 1
            else:
                multiplier >> 1
            
        return -quotient if negative else quotient
          
    # PASS 
    # Time:O(Log(n)) * O(Log(n)), Space: O(1)
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2147483647        # 2**31 - 1
        MIN_INT = -2147483648       # -2**31

        # Special case: overflow.
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        quotient = 0
        negative = False
        if divisor < 0:
            divisor *= -1
            negative = not negative
        if dividend < 0:
            dividend *= -1
            negative = not negative
        while dividend >= divisor:
            multiplier = 1
            value = divisor
            while value + value < dividend:
                value = value << 1
                multiplier = multiplier << 1
            quotient += multiplier
            dividend -= value
        return -quotient if negative else quotient
                

    # Time: O(Log(n)), Space: O(Log(n))
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2147483647        # 2**31 - 1
        MIN_INT = -2147483648       # -2**31

        # Special case: overflow.
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        quotient = 0
        negative = False
        if divisor < 0:
            divisor *= -1
            negative = not negative
        if dividend < 0:
            dividend *= -1
            negative = not negative
        
        # while dividend >= divisor:
        multiplier = 1
        value = divisor
        multiplier_list = [1]
        value_list = [divisor]
        while value + value <= dividend:
            value = value << 1
            multiplier = multiplier << 1
            value_list.append(value)
            multiplier_list.append(multiplier)
        for i in range(len(value_list)-1, -1, -1):
            if value_list[i] <= dividend:
                quotient += multiplier_list[i]
                dividend -= value_list[i]
        return -quotient if negative else quotient
