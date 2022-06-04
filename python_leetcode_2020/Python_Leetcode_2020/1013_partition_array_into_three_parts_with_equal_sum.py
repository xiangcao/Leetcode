"""
Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])
Input:
[10,-10,10,-10,10,-10,10,-10]
Output: false
Expected:  true
"""

class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        average, remainder, part, cnt = sum(A) // 3, sum(A) % 3, 0, 0
        for a in A:
            part += a
            if part == average:
                cnt += 1
                part = 0
        return not remainder and cnt >= 3
