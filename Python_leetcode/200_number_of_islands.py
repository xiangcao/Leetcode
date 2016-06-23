"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000

Answer: 1

Example 2:

11000
11000
00100
00011

Answer: 3
"""

class Solution(object):
    
    # Accepted
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # DFS
        if not len(grid) or not len(grid[0]):
            return 0
        maxRow = len(grid)
        maxCol = len(grid[0])
        visited = [[0 for j in range(maxCol)] for i in range(maxRow)]
        dir = [[0,1],[0,-1],[1,0],[-1,0]]   #方向向量，(x,y)周围的四个方向
        def check(x,y):
            if x < 0 or y < 0 or x >= maxRow or y >= maxCol:
                return False
            if grid[x][y] == '0' or visited[x][y]:
                return False
            return True
        def dfs(x, y):
            visited[x][y] = 1 
            for direction in dir:
                if check(x+direction[0], y + direction[1]):
                    dfs(x+direction[0], y + direction[1])
        count = 0 
        for i in range(maxRow):
            for j in range(maxCol):
                if check(i,j):
                    dfs(i,j)
                    count += 1
        return count
                    
               
    # Accepted 
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # DFS
        if not len(grid): #or not len(grid[0]):
            return 0
        maxRow = len(grid)
        maxCol = len(grid[0])
        visited = [[0 for j in range(maxCol)] for i in range(maxRow)]
        dir = [[0,1],[0,-1],[1,0],[-1,0]]   #direction vector，4 different direciton from (x,y)

        def dfs(x, y):
            if x < 0 or y < 0 or x >= maxRow or y >= maxCol:
                return False
            if grid[x][y] == '0' or visited[x][y]:
                return False
            visited[x][y] = 1 
            for direction in dir:
                    dfs(x+direction[0], y + direction[1])
            return True

        count = 0 
        for i in range(maxRow):
            for j in range(maxCol):
                    if dfs(i,j):
                        count += 1
        return count
            
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        #Union Find
        
        if not len(grid): #or not len(grid[0]):
            return 0
        maxRow = len(grid)
        maxCol = len(grid[0])
        id = [i for i in range(maxRow * maxCol)]
        self.count = sum([grid[i][j] == '1'  for i in range(maxRow) for j in range(maxCol) ])
        weight= [0 for i in range(maxRow * maxCol)]
        def find(i):
            while i != id[i]:
                id[i] = id[id[i]]
                i = id[i]
            return i
            
        def find_(i): # slower than the one above
            if i != id[i]:
                id[i] = find(id[i])
            return id[i]
        
        def union(i, j):
            iRoot = find(i)
            jRoot = find(j)
            if iRoot == jRoot:
                return
            else:
                if weight[iRoot] < weight[jRoot]:
                    id[iRoot] = jRoot
                elif weight[iRoot] > weight[jRoot]:
                    id[jRoot] = iRoot
                else:
                    id[iRoot] = jRoot
                    weight[jRoot] += 1
            self.count -= 1
            
        for i in range(maxRow):
            for j in range(maxCol):
                if grid[i][j] == '0': continue
                curNode = i * maxCol + j 
                if j < maxCol-1 and grid[i][j+1] == '1':
                    union(curNode, curNode + 1)
                if i < maxRow-1 and grid[i+1][j] == '1':
                    union(curNode, curNode + maxCol)
        return self.count
        
        
