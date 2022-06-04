"""
Given a positive integer K, you need to find the length of the smallest positive integer N such that N is divisible by K, and N only contains the digit 1.

Return the length of N. If there is no such N, return -1.

Note: N may not fit in a 64-bit signed integer.
"""
class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        remainder = 1
        for i in range(K):
            if remainder % K == 0:
                return i + 1
            remainder = (10 * remainder + 1) % K
        return -1
