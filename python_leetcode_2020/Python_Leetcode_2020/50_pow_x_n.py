"""
Implement pow(x, n), which calculates x raised to the power n (i.e. xn).
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        negative = False if n > 0 else True
        n = abs(n)
        extra = x if n % 2 else 1
        half = self.myPow(x, n//2)
        result = half * half * extra
        if negative:
            return 1/result
        else:
            return result
