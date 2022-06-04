class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -pow(2,31)
        INT_MAX = pow(2,31) - 1
        neg = x < 0
        result = 0
        if neg:
            x = -x
        while x:
            last = x % 10
            if result > INT_MAX // 10 or (not neg and result == INT_MAX //10 and last > 7) or (neg and result == INT_MAX //10 and last > 8):
                return 0
            result = result * 10 + last
            x = x // 10
        if neg:
            result = -result
        #if result < INT_MIN or result > INT_MAX:
        #    return 0
        return result
            
