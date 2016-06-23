"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.

For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

Given target = 5, return true.

Given target = 20, return false

"""
class Solution(object):
    def searchMatrix_1(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        maxRow, maxCol = len(matrix), len(matrix[0])
        row, col = 0, maxCol-1
        while row < maxRow:
            while matrix[row][col] > target and col > 0:
                col -= 1
            if matrix[row][col] == target:
                return True
            row += 1
        return False
        
                
    def searchMatrix_2(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        maxRow, maxCol = len(matrix), len(matrix[0])
        def binarySearch(nums, left, right):
            while left <= right:
                mid = left + (right-left)/2 
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1 
            return left
            
        for row in range(maxRow):
            y = binarySearch(matrix[row], 0, maxCol-1)
            if y<maxCol and matrix[row][y] == target:
                return True
        return False

    def searchMatrix(self, matrix, target):
        y = len(matrix[0]) - 1
        def binSearch(nums, low, high):
            while low <= high:
                mid = (low + high) / 2
                if nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return high
        for x in range(len(matrix)):
            y = binSearch(matrix[x], 0, y)
            if matrix[x][y] == target:
                return True
        return False
