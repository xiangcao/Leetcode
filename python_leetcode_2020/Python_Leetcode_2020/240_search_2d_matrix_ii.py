"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
"""

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        r = len(matrix)-1
        c = 0
        
        while r >= 0 and c < len(matrix[0]):
            value = matrix[r][c]
            if value == target:
                return True
            if value > target:
                r -= 1
            else:
                c += 1
        return False
            
        
