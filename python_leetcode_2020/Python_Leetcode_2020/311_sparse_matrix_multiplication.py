"""
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.
"""

class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        
        m, n, nB = len(A), len(A[0]), len(B[0])

        C = [[0] * nB for i in range(m)] 
        for i in range(m):
            for k in range(n):
                if (A[i][k] != 0):
                    for j in range(nB):
                        if (B[k][j] != 0):
                            C[i][j] += A[i][k] * B[k][j]
        return C

""" Analsysis ******
Let's look at brute force solution:

public int[][] multiply_bruteForce(int[][] A, int[][] B) {
	int m = A.length, n = A[0].length;
	int nB = B[0].length;
	int [][] C = new int[m][nB];
	for (int i = 0; i<m; i++) {
		for (int j = 0; j<nB; j++){
			C[i][j] = 0;
			for( int k = 0; k<n; k++)
				C[i][j] += A[i][k]*B[k][j];
		}
	}
	return C;
}
For brute force solution, for each C[ i ] [ j ], it uses C[ i ] [ j ] += A[ i ] [ k ] * B[ k ] [ j ] where k = [ 0, n].Note: even A[ i ] [ k ] or B[ k ] [ j ] is 0, the multiplication is still executed.

For the above smart solution, if A[ i ] [ k ] == 0 or B[ k ] [ j ] == 0, it just skip the multiplication . This is achieved by moving for-loop" for ( k = 0; k < n; k++ ) " from inner-most loop to middle loop, so that we can use if-statement to tell whether A[ i ] [ k ] == 0 or B[ k ] [ j ] == 0. This is really smart. Thanks @yavinci
"""
