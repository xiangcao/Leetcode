"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
"""

class Solution(object):
    
    #Wrong!!!
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
         Input: 30
         Output: 6
         Expected: 7 
        """
        count = 0
        while n:
            if n / 10 >= 1:
                count += 2 * (n/10)
                n %= 10
            elif n >= 5:
                count += 1
                break
            else:
                break
        return count
        
    def trailingZeroes(self, n):
        count = 0 
        while n:
            count += n/5
            n = n/5
        return count
        
    def trailingZeroes_(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.trailingZeroes(n/5) + n/5 if n else 0
        
