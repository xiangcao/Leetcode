class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        right = rows * cols - 1
        left = 0 
        while left <= right:
            mid = (left + right) // 2
            value = matrix[mid//cols][mid%cols]
            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
            
