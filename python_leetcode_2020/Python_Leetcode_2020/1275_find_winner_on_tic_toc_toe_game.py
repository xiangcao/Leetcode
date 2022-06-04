"""
Tic-tac-toe is played by two players A and B on a 3 x 3 grid.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player A always places "X" characters, while the second player B always places "O" characters.
"X" and "O" characters are always placed into empty squares, never on filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given an array moves where each element is another array of size 2 corresponding to the row and column of the grid where they mark their respective character in the order in which A and B play.

Return the winner of the game if it exists (A or B), in case the game ends in a draw return "Draw", if there are still movements to play return "Pending".

You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the grid is initially empty and A will play first.
"""

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows = [0] * 3
        cols = [0] * 3
        diag = 0
        anti_diag = 0
        i = 0
        for r,c in moves:
            change = 1 if i % 2 else -1
            rows[r] += change
            cols[c] += change
            if r == c:
                diag += change
            if r + c == 2:
                anti_diag += change

            if abs(rows[r]) == 3 or abs(cols[c]) == 3 or abs(diag) == 3 or abs(anti_diag) == 3:
                return 'B' if i % 2 else 'A'
            i += 1
        return 'Pending' if i < 9 else 'Draw'
                
            
