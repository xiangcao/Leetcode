class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.board = [['-' for i in range(n)] for j in range(n)]
        self.rows = [0 for i in range(n)]
        self.cols = [0 for i in range(n)]
        self.diag = 0
        self.anti_diag = 0
        self.size = n

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        if player == 1:
            self.rows[row] += -1
            self.cols[col] += -1
            self.diag += -1 * (row == col)
            self.anti_diag += -1 * (row+col == self.size-1)
            
            if -self.size in [self.rows[row], self.cols[col], self.diag, self.anti_diag]:
                return 1

        elif player == 2:
            self.rows[row] += 1
            self.cols[col] += 1
            self.diag += 1 * (row == col)
            self.anti_diag += 1 * (row+col == self.size-1)
            if self.size in [self.rows[row], self.cols[col], self.diag, self.anti_diag]:
                return 2
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
