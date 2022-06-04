"""
You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position to the left, 1 position to the right in the array or stay in the same place  (The pointer should not be placed outside the array at any time).

Given two integers steps and arrLen, return the number of ways such that your pointer still at index 0 after exactly steps steps.

Since the answer may be too large, return it modulo 10^9 + 7.
"""

class Solution:
    def __init__(self):
        self.MOD = 10 ** 9 + 7
    # memoization
    # Complexity
    # Space: O(steps^2). This can be reduecd to O(steps) by using top-down DP.
    # Time: O(steps^2).
    def numWays(self, steps: int, arrLen: int) -> int:
        mem = [[-1] * (steps+1) for _ in range(steps//2+1)]
        def help(pos, steps):
            if pos ==0 and steps == 0:
                return 1
            if pos < 0 or pos >= arrLen or steps == 0 or pos > steps:
                return 0
            if mem[pos][steps] != -1:
                return mem[pos][steps]
            mem[pos][steps] = ((help(pos + 1, steps-1)  + help(pos - 1, steps - 1)) + help(pos, steps-1)) % self.MOD
            return mem[pos][steps]
        return help(0, steps)
    
    # Bottom up
    # Time: O(n * min(n, m)), where n is the number of steps, and m - array size.
    # Memory: O(min(n, m)).
    # The array size can be larger than the number of steps. We can ingore array elements greater than steps / 2, as we won't able to go back to the first element from there.
    def numWays(self, steps: int, arrLen: int) -> int:
        sz = min(steps // 2 + 1, arrLen)
        v1 = [0] * (sz+2)
        v2 = [0] * (sz+2)
        
        v1[1] = 1
        while (steps > 0):
            for i in range(1, sz+1): # i: ith position in the array
                v2[i] = (v1[i] + v1[i - 1] + v1[i + 1]) % 1000000007
            v1, v2 = v2, v1
            steps -= 1
        return v1[1]
