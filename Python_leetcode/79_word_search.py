#一遍就accept了。
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        maxRow = len(board)
        maxCol = len(board[0])
        used = set()
        def dfs(i, j, used, curstr):
            
            if word == curstr:
                return True
            if not word.startswith(curstr):
                return False
            for row,col in [(i-1,j), (i+1, j), (i,j-1), (i,j+1)]:
                if row < 0 or col < 0 or row >= maxRow or \
                   col >= maxCol or (row,col) in used:
                    continue
                used.add((row,col))
                if dfs(row, col, used, curstr+board[row][col]):
                    return True
                used.remove((row,col))
        
        for row in range(maxRow):
            for col in range(maxCol):
                used.add((row,col))
                if dfs(row, col, used, board[row][col]):
                    return True
                used.remove((row,col))
        return False
            
