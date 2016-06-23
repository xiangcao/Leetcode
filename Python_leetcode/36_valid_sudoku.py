class Solution(object):
    #pass
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        def verify(row, col, value):
            if value == '.':
                return True
            for i in range(row):
                if board[i][col] == value:
                    return False
            for j in range(col):
                if board[row][j] == value:
                    return False
            toprow = (row / 3) * 3 
            leftcol = (col / 3) * 3 
            for i in range(toprow, toprow+3):
                for j in range(leftcol, leftcol+3):
                    if board[i][j] == value and i != row and j != col:
                        return False
            return True
            
        rowlength = len(board)
        collength = len(board[0])
        
        for i in range(rowlength):
            for j in range(collength):
                if not verify(i, j, board[i][j]):
                    return False
        return True           



class Solution(object):
    #pass
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        def verify(row, col, value):
            if value == '.':
                return True
            for i in range(rowlength):
                if board[i][col] == value and i != row:
                    return False
            for j in range(collength):
                if board[row][j] == value and j != col:
                    return False
            toprow = (row / 3) * 3 
            leftcol = (col / 3) * 3 
            for i in range(toprow, toprow+3):
                for j in range(leftcol, leftcol+3):
                    if board[i][j] == value and i != row and j != col:
                        return False
            return True
            
        rowlength = len(board)
        collength = len(board[0])
        
        for i in range(rowlength):
            for j in range(collength):
                if not verify(i, j, board[i][j]):
                    return False
        return True
            
