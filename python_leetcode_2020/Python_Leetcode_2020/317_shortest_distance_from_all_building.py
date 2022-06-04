import collections
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M, N = len(grid), len(grid[0])
        buildings = sum(1 for i in range(M) for j in range(N) if grid[i][j] == 1)
        distSum = [[0] * N for i in range(M)]
        hits = [[0] * N for i in range(M)]
        self.buildings_completed = 0
        def bfs(x, y):
            visited = [[False] * N for i in range(M)]
            visited[x][y] = True
            count = 1
            queue = collections.deque([(x,y,0)])
            
            while queue:
                pre_x, pre_y, pre_dist = queue.popleft()
                for i, j in ((pre_x, pre_y-1), (pre_x, pre_y+1), (pre_x-1, pre_y), (pre_x+1, pre_y)):
                    if i < 0 or j < 0 or i >= M or j >= N or visited[i][j]:
                        continue
                    visited[i][j] = True
                    if grid[i][j] == 1:
                       count += 1
                    if hits[i][j] <  self.buildings_completed:
                        continue
                    if grid[i][j] == 0:
                        hits[i][j] += 1
                        distSum[i][j] += pre_dist + 1
                        queue.append((i, j, pre_dist+1))
            return count == buildings

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    if not bfs(i, j):
                        return -1 
                    self.buildings_completed += 1
        return min([distSum[i][j] for i in range(M) for j in range(N) if not grid[i][j] and hits[i][j] == buildings] or [-1])
    
sol = Solution()
grid=[[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
print("result: %s" %sol.shortestDistance(grid))

Does anyone want to ask Why don't we start from '0'? This is also what I am thinking. At the first glance, the time complexity of starting from buildings O(B*M*N) (B: # of buildings) and starting from empty places O(E*M*N) (E: # of empty places) might be the same. If in an interview, I think we can ask for clarification. If the empty places are far more than buildings, ex. we have 1 million empty places and only 1 building, starting from building is better. So it depends on how many empty places and buildings that we have. We are not going to say this way or that way is better, but it's a kind of trade-off.

Answer:
No. Start from building is always better.
If you think carefully you will find that "Start from buildings" is actually equivalent to dynamic programming, but without using memoization (namely, it's equivalent to "start from '0's" with memoization). So there is least number of repeated computation in this approach. But start from "0"s, would result in a lot of repeated computation of the same value, if without memoization.

Anyway, this fact is not so apparent. I'm just pointing this out but it requires some reasoning before you begin to see through.
