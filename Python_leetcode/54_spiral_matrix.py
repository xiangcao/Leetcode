class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if m == 0: return []
        n = len(matrix[0])
        
        colLeft,colRight,rowTop,rowBottom = (0,n-1,0,m-1)
        x = 0
        y = 0
        result = []
        direction = 1 #1:right, 2: Down, 3:Left, 4: Up
        while True:
            if colLeft > colRight or rowTop > rowBottom:# or x > m-1 or x < 0 or y > n-1 or y <0:
                return result
            result.append(matrix[x][y])
            if direction == 1:
                if y < colRight:
                   y = y +1
                else:
                   direction = 2
                   rowTop += 1
                   #colRight -= 1
                   x += 1

            elif direction == 2:
                if x < rowBottom:
                    x += 1
                else:
                    direction = 3
                    colRight -= 1
                    #rowBottom -= 1
                    y -= 1

            elif direction == 3:
                if y > colLeft:
                    y -= 1
                else:
                    direction = 4
                    rowBottom -= 1
                    #colLeft += 1
                    x -= 1

            elif direction == 4:
                if x > rowTop:
                    x -= 1
                else:
                    direction = 1
                    colLeft += 1
                    #rowTop += 1
                    y += 1
   
   
'''
A better solution.
http://www.cnblogs.com/zuoyuan/p/3769829.html
class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if matrix == []: return []
        up = 0; left = 0
        down = len(matrix)-1
        right = len(matrix[0])-1
        direct = 0  # 0: go right   1: go down  2: go left  3: go up
        res = []
        while True:
            if direct == 0:
                for i in range(left, right+1):
                    res.append(matrix[up][i])
                up += 1
            if direct == 1:
                for i in range(up, down+1):
                    res.append(matrix[i][right])
                right -= 1
            if direct == 2:
                for i in range(right, left-1, -1):
                    res.append(matrix[down][i])
                down -= 1
            if direct == 3:
                for i in range(down, up-1, -1):
                    res.append(matrix[i][left])
                left += 1
            if up > down or left > right: return res
            direct = (direct+1) % 4


'''
                
            
