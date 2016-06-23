class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        numRow = len(board)
        if numRow == 0:
            return
        numCol = len(board[0])
        count=[[0 for j in range(numCol)] for i in range(numRow)]
        def increaseCount( i, j):
            if i < numRow and j < numCol and i >= 0 and j >=0:
                count[i][j] += 1

        for row in range(numRow):
            for col in range(numCol):
                if board[row][col] == 1:
                        increaseCount(row-1,col)
                        increaseCount(row-1,col-1)
                        increaseCount(row-1,col+1)
                        increaseCount(row,col+1)
                        increaseCount(row,col-1)
                        increaseCount(row+1,col)
                        increaseCount(row+1,col-1)
                        increaseCount(row+1,col+1)
      
        for row in range(numRow):
            for col in range(numCol):
                print count[row][col]
                if count[row][col] < 2 or count[row][col] >3:
                    board[row][col] = 0
                elif count[row][col] == 3:
                    board[row][col] = 1

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        #0:dead become dead
        #1:live become live
        #2:live become dead
        #3:dead become live
        numRow = len(board)
        if numRow == 0:
            return
        numCol = len(board[0])
        for row in range(numRow):
            for col in range(numCol):
                count = 0
                rowUp = max(0, row-1)
                rowBottom = min(numRow-1, row+1)
                for i in range(rowUp, rowBottom+1):
                    colLeft = max(0, col-1)
                    colRight = min(numCol-1, col+1)
                    for j in range(colLeft, colRight+1):
                        if (i != row or j != col) and (board[i][j] == 1 or board[i][j] == 2):
                            count += 1
                if board[row][col] == 1 and (count<2 or count>3):
                    board[row][col] = 2
                elif board[row][col] == 0 and count == 3:
                    board[row][col] = 3
                    
        for row in range(numRow):
            for col in range(numCol):
                board[row][col] %= 2
           

    # bitwise operator to encode the different state
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        numRow = len(board)
        if numRow == 0:
            return
        numCol = len(board[0])
        for row in range(numRow):
            rowUp = max(0, row-1)
            rowBottom = min(numRow-1, row+1)
            for col in range(numCol):
                count = 0
                for i in range(rowUp, rowBottom+1):
                    colLeft = max(0, col-1)
                    colRight = min(numCol-1, col+1)
                    for j in range(colLeft, colRight+1):
                        count += board[i][j] & 1
                if(count == 3 or count - board[row][col] == 3):
                    board[row][col] |= 2
        for row in range(numRow):
            for col in range(numCol):
                board[row][col] >>=1

sol = Solution()
board=[[1,1],[1,0]]
sol.gameOfLife(board)
"""
others' code
http://www.cnblogs.com/grandyang/p/4854466.html
https://segmentfault.com/a/1190000003819277: 附含多种解法
http://bookshadow.com/weblog/2015/10/04/leetcode-game-life/ 
""" 
