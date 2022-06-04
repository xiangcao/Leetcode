"""
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.

Note:

matrix will be a 2D array of integers.
matrix will have a number of rows and columns in range [1, 20].
matrix[i][j] will be integers in range [0, 99].

Follow up:

What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
What if the matrix is so large that you can only load up a partial row into the memory at once?

"""

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return all(r== 0 or c == 0 or matrix[r-1][c-1] == matrix[r][c] 
                   for r in range(len(matrix))
                   for c in range(len(matrix[0])))
    
        # follow up 1:
      """
        What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
        
        For the follow-up 1, we are only able to load one row at one time, so we have to use a buffer (1D data structure) to store the row info. When next row comes as a streaming flow, we can compare each value (say, matrix[i][j], i>=1, j>=1) to the "upper-left" value in the buffer (buffer[j - 1]); meanwhile, we update the buffer by inserting the 1st element of the current row (matrix[i][0]) to buffer at position 0 (buffer[0]), and removing the last element in the buffer."""
 
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if not matrix: return True
        row, col = len(matrix), len(matrix[0])
        buffer = collections.deque(matrix[0])
        for i in range(1, row):
            buffer.pop()
            buffer.appendleft(matrix[i][0])
            if any(buffer[j] != matrix[i][j] for j in range(col)):
                return False
        return True
            
      """For the follow-up 2, we can only load a partial row at one time. We could split the whole matrix vertically into several sub-matrices, while each sub-matrix should have one column overlapped. We repeat the same method in follow-up 1 for each sub-matrix."""
[1 2 3 4 5 6 7 8 9 0]              [1 2 3 4]              [4 5 6 7]              [7 8 9 0]
[0 1 2 3 4 5 6 7 8 9]              [0 1 2 3]              [3 4 5 6]              [6 7 8 9]
[1 0 1 2 3 4 5 6 7 8]     -->      [1 0 1 2]       +      [2 3 4 5]       +      [5 6 7 8]
[2 1 0 1 2 3 4 5 6 7]              [2 1 0 1]              [1 2 3 4]              [4 5 6 7]
[3 2 1 0 1 2 3 4 5 6]              [3 2 1 0]              [0 1 2 3]              [3 4 5 6]




Second idea for follow up:
No online judge for the follow-up questions so let's discuss:
1. What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
Compare half of 1 row with half of the next/previous row.
2. What if the matrix is so large that you can only load up a partial row into the memory at once?
Hash 2 rows (so only 1 element needs to be loaded at a time) and compare the results, excluding the appropriate beginning or ending element.

Other ideas?
