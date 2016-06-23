"""
 You are given a m x n 2D grid initialized with these three possible values.

    -1 - A wall or an obstacle.
    0 - A gate.
    INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF

After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""



class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        # The Multi End BFS solution used is this
        INF = 2**31-1
        dirVector = [(0,1), (0,-1), (1, 0), (-1, 0)]
        
        queue = collections.deque([(i,j) for i, row in enumerate(rooms) for j, room in enumerate(row) if room == 0] )
        
        
        while queue:
            room = queue.pop()
            i, j = room[0], room[1]
            
            for dir in dirVector:
                nextI, nextJ = i+dir[0], j+dir[1]
                if 0<=nextI<len(rooms) and 0 <= nextJ < len(rooms[0]) and rooms[nextI][nextJ] == INF:
                    rooms[nextI][nextJ] = rooms[i][j] + 1
                    queue.appendleft((nextI, nextJ))
                
        
    # refer https://leetcode.com/discuss/82264/benchmarks-of-dfs-and-bfs 
        
        
