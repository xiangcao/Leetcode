"""
Given a square grid of integers arr, a falling path with non-zero shifts is a choice of exactly one element from each row of arr, such that no two elements chosen in adjacent rows are in the same column.

Return the minimum sum of a falling path with non-zero shifts.
"""

class Solution(object):
    # Find the 2 minimum value in the previous row.
    # DP
    def minFallingPathSum(self, arr):
        """
        :type arr: List[List[int]]
        :rtype: int
        """
        A = arr
        for i in xrange(1, len(A)):
            r = heapq.nsmallest(2, A[i - 1])
            for j in range(len(A[0])):
                A[i][j] += r[1] if r[0] == A[i-1][j] else r[0]
        return min(A[-1])
