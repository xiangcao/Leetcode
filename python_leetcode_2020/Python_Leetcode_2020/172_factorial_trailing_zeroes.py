"""
Given an integer n, return the number of trailing zeroes in n!.

Follow up: Could you write a solution that works in logarithmic time complexity?
"""
class Solution:
    
    # power_of_5 may overflow when multiplying with 5 in non-python solution
    def trailingZeroes(self, n: int) -> int:
        count = 0
        power_of_5 = 5
        while n >= power_of_5:
            count += n // power_of_5
            power_of_5 *= 5
        return count
    
    # Optimize: to avoid overflow
    def trailingZeroes(self, n: int) -> int:
        count = 0
        power_of_5 = 5
        while n >= power_of_5:
            count += n // power_of_5
            n = n // power_of_5
        return count
