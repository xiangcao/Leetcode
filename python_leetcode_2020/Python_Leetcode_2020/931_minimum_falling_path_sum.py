"""
Given a square array of integers A, we want the minimum sum of a falling path through A.

A falling path starts at any element in the first row, and chooses one element from each row.  The next row's choice must be in a column that is different from the previous row's column by at most one.
 
"""
class Solution(object):
    # DP O(n*n)
    """
	The minimum path to get to element A[i][j] is the minimum of A[i - 1][j - 1], A[i - 1][j] and A[i - 1][j + 1].
	Starting from row 1, we add the minumum path to each element. The smallest number in the last row is the miminum path sum.
	Example:
	[1, 2, 3]
	[4, 5, 6] => [5, 6, 8]
	[7, 8, 9] => [7, 8, 9] => [12, 13, 15]
    """
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        for i in range(1, len(A)):
            for j in range(len(A[0])):
                A[i][j] += min(A[i-1][j], A[i-1][max(0,j-1)], A[i-1][min(j+1, len(A)-1)])
        return min(A[-1])
