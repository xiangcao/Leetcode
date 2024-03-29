"""
Count the number of prime numbers less than a non-negative number, n.

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False
        for i in range(2, int(math.sqrt(n))+1):
            if isPrime[i]:
                for j in range(i*i, n, i):
                    isPrime[j] = False
        
        return isPrime.count(True)
