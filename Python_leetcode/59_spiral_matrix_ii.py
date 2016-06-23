"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,
You should return the following matrix:

[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

"""
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for j in range(n)] for i in range(n)]
        i, j = 0, 0
        direction = 0 #0: right, 1: down, 2:left, 3:up
        colLeft,colRight,rowTop,rowBottom = (0,n-1,0,n-1)
        k = 1
        while True:
            if colLeft > colRight or rowTop > rowBottom:
                return matrix
            matrix[i][j] = k
            k += 1
            if direction == 0:
                if j < colRight:
                    j += 1
                else:
                    i += 1
                    direction = (direction + 1)%4
                    rowTop += 1
            elif direction == 1:
                if i < rowBottom:
                    i += 1
                else:
                    j -= 1
                    direction = (direction + 1)%4 
                    colRight -= 1
            elif direction == 2:
                if j > colLeft:
                    j -= 1
                else:
                    i -= 1
                    direction = (direction + 1)%4
                    rowBottom -= 1
            else:
                if i > rowTop:
                    i -= 1
                else:
                    j += 1
                    direction = (direction + 1)%4
                    colLeft += 1
                
        
