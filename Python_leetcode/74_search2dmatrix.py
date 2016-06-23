class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        maxRow = len(matrix)
        maxCol = len(matrix[0])
        
        maxPosition = maxRow * maxCol - 1
        
        left, right = 0, maxPosition
        
        while left < right:
            middle = left + (right - left)/2 
            row = middle / maxCol
            col = middle % maxCol
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = middle - 1
            else:
                left = middle + 1
        if matrix[left/maxCol][left%maxCol] == target:
            return True
        return False
