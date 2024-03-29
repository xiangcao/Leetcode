"""
Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        def next(n):
            result = 0
            while n > 0:
                lastdigit = n % 10
                result += pow(lastdigit, 2)
                n = n // 10
            return result
        
        slow = fast = n
        while fast != 1:
            slow = next(slow)
            fast = next(next(fast))
            if slow == fast:
                break
        return fast == 1
