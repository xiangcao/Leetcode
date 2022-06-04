"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        def backtrack(row, col, suffix):
            if len(suffix) == 0:
                return True
            if row < 0 or col < 0 or row == rows or col == cols or board[row][col] != suffix[0]:
                return False
            board[row][col] = '#'
            for rowdiff, coldiff in [(0,1), (0, -1), (1,0), (-1,0)]:
                if backtrack(row+rowdiff, col+coldiff, suffix[1:]):
                    board[row][col] = suffix[0]
                    return True
            board[row][col] = suffix[0]
            return False
        
        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, word):
                    return True
        return False

    # slight modification. pass index to backtrack method instead of creating substring each time
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        def backtrack(row, col, index):
            if index == len(word):
                return True
            if row < 0 or col < 0 or row == rows or col == cols or board[row][col] != word[index]:
                return False
            board[row][col] = '#'
            for rowdiff, coldiff in [(0,1), (0, -1), (1,0), (-1,0)]:
                if backtrack(row+rowdiff, col+coldiff, index+1):
                    board[row][col] = word[index]
                    return True
            board[row][col] = word[index]
            return False

        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True
        return False
