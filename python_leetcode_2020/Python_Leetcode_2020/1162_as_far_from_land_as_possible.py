"""
Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized and return the distance.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

If no land or water exists in the grid, return -1.

 
"""

class Solution:
    # use the code from Wall and Gates. 
    # 644 ms > 60%
    def maxDistance1(self, grid: List[List[int]]) -> int:
        rooms = grid
        if not rooms:
            return
        m, n = len(rooms), len(rooms[0])
        queue = collections.deque()
       
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 1:
                    queue.append((i,j))

        if len(queue) == m * n  or len(queue) == 0:
            return -1

        def nextPos(i, j):
            for di, dj in [(0,1), (0, -1), (1, 0), (-1, 0)]:
                yield (i+di, j + dj)
     
        while queue:
            x, y = queue.popleft()
            
            for new_x, new_y in nextPos(x, y):
                if new_x < 0 or new_y < 0 or new_x >= m or new_y >= n or rooms[new_x][new_y] != 0:
                    continue
                rooms[new_x][new_y] = rooms[x][y] + 1
                queue.append((new_x, new_y))
        return max(rooms[i][j]-1 for i in range(m) for j in range(n) if rooms[i][j] != 0 )
    
    # 504 ms > 97%
    def maxDistance(self, grid: List[List[int]]) -> int:
        if not grid:
            return
        m, n = len(grid), len(grid[0])
        queue = collections.deque()
       
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i,j))

        #if len(queue) == m * n  or len(queue) == 0:
        #    return -1
        
        step = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                for nextI, nextJ in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= nextI < m and 0 <= nextJ < n and grid[nextI][nextJ] == 0:
                        queue.append((nextI, nextJ))
                        grid[nextI][nextJ] = 1
            step += 1
        return step - 1 or -1
    
Explanation:
given an n by n matrix with 1s (land) and 0s (water) we have to " find a water cell such that its distance to the nearest land cell is maximized ". The question can be rephrased in simpler words. Every water cell has a shortest distance to a land cell. Which one of these shortest distances has the highest value;

To find this we can find the shortest distance of each 0 to a 1.
Before that, a matrix can be represented as an unweighted undirected graph. A good way to find the shortest distance on a unweighted graph is bfs.(visit nodes of distance 1 from source then distance 2 from source then distance 3 ....)

there are 2 ways to do this :- either start a bfs from every water node or start a bfs from every land node
if the first approach is chosen, we have to do a bfs from every water node and store the result.
this means we have to traverse the graph upto n^2 times which gives it a worst case complexity of O(n^4)
(btw is there any way of using dynamic programming to reduce this into a O(n^2) algorithm)

the second approach doesnt seem too different from the first as we may have to traverse the entire matrix n^2
times. That is the case if we were to start a bfs from every land node individually;

However if we start the bfs from every land node simultaneously, we will only process each node upto 2 times.
what i mean is , in the first step , queue all the 1s (level 0) then queue all the neighbours of the 1s(level 1)
then queue all of their neighbours(level 2) ....and in each step queue only 0s which have already not been
visited because
the 0s which have been visited have a shorter path to a 1 (as bfs visits the 0s level by level, the first time u
visit a 0 assign a level to it, will be the lowest one (shortest distance)).
the last 0 u queue will have the largest shortest distance .
visually this is how the algorithm would run
