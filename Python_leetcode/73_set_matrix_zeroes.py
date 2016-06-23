"""
 Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.
Follow up:

Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # change the beginning of each column or row to zero to mark this column/row should be zeroed
        
        maxRow = len(matrix)
        maxCol = len(matrix[0])
        firstRowZero, firstColZero = False, False
        for i in range(maxRow):
            if matrix[i][0] == 0:
                firstColZero = True
                break
        for j in range(maxCol):
            if matrix[0][j] == 0:
                firstRowZero = True

        for i in range(1,maxRow):
            for j in range(1,maxCol):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1,maxRow):
            for j in range(1,maxCol):
                if matrix[0][j]==0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if firstColZero:
            for i in range(maxRow):
                matrix[i][0] = 0 
        if firstRowZero:
            for j in range(maxCol):
                matrix[0][j] = 0
        
            

