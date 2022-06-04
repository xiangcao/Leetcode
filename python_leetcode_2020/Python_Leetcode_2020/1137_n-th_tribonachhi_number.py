"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        if n == 2:
            return 1
        first, second = 1, 1
        cur = 2
        for i in range(4, n+1):
            temp = cur
            cur = first + second + cur
            first = second
            second = temp

        return cur
    
    def tribonacci2(self, n: int) -> int:
        if n < 3:
            return 1 if n else 0
        
        x, y, z = 0, 1, 1
        for _ in range(n - 2):
            x, y, z = y, z, x + y + z
        return z
