class Solution:
    def hammingWeight1(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n = n >> 1
        return count
    
    def hammingWeight(self, n: int) -> int:
        c = 0
        while n:
            n &= n - 1
            c += 1
        return c
