"""
52.
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return the number of distinct solutions to the n-queens puzzle.
"""
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.count = 0
        self.placeQueen([-1]*n, 0, n);
        return self.count

    def placeQueen(self, board, row, nQueens):
        if (row == nQueens):
            self.count += 1
            return

        for i in range(nQueens):
            board[row] = i
            if (self.isValid(board, row)):
                self.placeQueen(board, row + 1, nQueens)

    def isValid(self, board, row):
        for i in range(row):
            if (board[i] == board[row] or row - i == abs(board[i] - board[row])):
                return False
        return True

"""
51:
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.result=[]
        self.placeQueen([-1]*n, 0, n);
        return self.result

    def constructResult(self, board):
        solution = [["."]*len(board) for row in range(len(board))]
        for row in range(len(board)):
            solution[row][board[row]] = 'Q'
        return ["".join(row) for row in solution]

    def placeQueen(self, board, row, nQueens):
        if (row == nQueens):
            self.result.append(self.constructResult(board))
            return

        for i in range(nQueens):
            board[row] = i
            if (self.isValid(board, row)):
                self.placeQueen(board, row + 1, nQueens)

    def isValid(self, board, row):
        for i in range(row):
            if (board[i] == board[row] or row - i == abs(board[i] - board[row])):
                return False
        return True
