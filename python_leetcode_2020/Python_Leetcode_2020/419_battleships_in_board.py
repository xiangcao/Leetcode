"""
Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:
You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
"""

class Solution(object):
   """
   Going over all cells, we can count only those that are the "first" cell of the battleship. First cell will be defined as the most top-left cell. We can check for first cells by only counting cells that do not have an 'X' to the left and do not have an 'X' above them.
   """
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board:
            return 0
        m, n = len(board), len(board[0])
        
        count=0;
        
        for i in range(m):
            for j in range(n):
                if (board[i][j] == '.'): continue
                if (i > 0 and board[i-1][j] == 'X'): continue
                if (j > 0 and board[i][j-1] == 'X'): continue
                count += 1
        
        return count
