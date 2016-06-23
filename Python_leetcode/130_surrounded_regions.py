class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        #BFS refer https://leetcode.com/discuss/45746/9-lines-python-148-ms
        # https://leetcode.com/discuss/6285/solve-it-using-union-find
        maxRow = len(board)
        if not maxRow:
            return
        maxCol = len(board[0])
        queue = [ij for k in range(max(maxRow, maxCol)) \
                                 for ij in ((0,k),(maxRow-1,k),(k, 0), (k, maxCol-1))]
        def bfs():
            while queue:
                row, col = queue.pop()
                if maxRow > row >= 0 and maxCol > col >= 0 and board[row][col] == 'O':
                    board[row][col] = 'B'
                    queue.extend([(row, col+1), (row, col-1), (row-1, col), (row+1,col)])
        
        bfs()
        board[:] = [["XO"[c=='B'] for c in row] for row in board]
