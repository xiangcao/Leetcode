class Solution(object):
    #pass
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        maxrow = len(board)
        maxcol = len(board[0])
        def judge(row, col, value):
            print "in judge: row %s, col %s, value %s" %(row, col, value)
            for i in range(maxrow):
                if board[i][col] == value and i != row:
                    return False
            for j in range(maxcol):
                print value, board[row][j]
                if board[row][j] == value and j != col:
                    return False
            
            toprow = (row/3)*3
            leftcol = (col/3)*3
            for i in range(toprow, toprow+3 ):
                for j in range(leftcol, leftcol+3):
                    if board[i][j] == value and i != row and j != col:
                        return False
            return True
        
        def dfs(row, col):
            if col >= 9:
                return dfs(row+1, 0)
            if row == 9:
                return True
            if board[row][col] != '.':
                return dfs(row, col+1)
            for k in range(1, 10):
                digit = str(k)
                if judge(row, col, digit):
                    board[row][col] = digit
                    print board
                    raw_input()
                    if dfs(row, col+1): return True
                    board[row][col] = '.'
            return False
    
        dfs(0,0)
                    


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        maxrow = len(board)
        maxcol = len(board[0])
        def judge(row, col, value):
            for i in range(maxrow):
                if board[i][col] == value and i != row:
                    return False
            for j in range(maxcol):
                if board[row][j] == value and j != col:
                    return False
            toprow = (row/3)*3
            leftcol = (col/3)*3
            for i in range(3):
                for j in range(3):
                    if board[i+toprow][j+leftcol] == value and i+toprow != row and j+leftcol != col:
                        return False
            return True

        def dfs():
            for i in range(maxrow):
                for j in range(maxcol):
                    if board[i][j] != '.':
                        continue
                    for k in range(1, 10):
                        digit = str(k)
                        if judge(i, j, digit):
                            board[i][j] = digit
                            if dfs(): return True
                            board[i][j] = '.'
                    return False
            return True

        dfs()

sol = Solution()
board=["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
board=[[i for i in string] for string in board]
sol.solveSudoku(board)

