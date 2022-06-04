"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1
"""
# https://leetcode.com/problems/sum-of-two-integers/discuss/132479/Simple-explanation-on-how-to-arrive-at-the-solution

https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary%3A-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        
        max_int = 0x7FFFFFFF
        return a if a < max_int else ~(a ^ mask)


class Solution:
    # does not work for test case: a:1, b:-1
    def getSum(self, a: int, b: int) -> int:
        c = 0
        while(b !=0 ):
            c = (a&b)
            a = a ^ b
            b = (c)<<1
        return a
