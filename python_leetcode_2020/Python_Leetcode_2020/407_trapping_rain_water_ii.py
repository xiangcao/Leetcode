"""
Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.


Answer:
1. Just like 1-D two pointer approach, we need to find some boundary. Because all boundary cells cannot hold any water for sure, we use them as the initial boundary naturally.

2. Then which bar to start? Find the min bar (let's call it A) on the boundary (heap is a natural choice), then do 1 BFS (4 directions). Why BFS? Because we are sure that the amount of water that A's neighbors can hold is only determined by A now for the same reason in 1D two-pointer approach.

3. How to update the heap during BFS
Step 1. Remove the min bar A from the heap
Step 2. If A's neighbor B's height is higher, it cannot hold any water. Add it to the heap
Step 3. If B's height is lower, it can hold water and the amount of water should be height_A - height_B. Here comes the tricky part, we still add B's coordinate into the heap, BUT change its height to A's height because A is the max value along this path (for this reason we cannot just use heightMap and need a class/array to store it's coordinates and UPDATED height). And we can think of B as a replacement of A now and never worry about A again. Therefore a new boundary is formed and we can repeat this process again.
"""    
def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        
        import heapq    
        m, n = len(heightMap), len(heightMap[0])
        heap = []
        visited = [[0]*n for _ in xrange(m)]

        # Push all the block on the border into heap
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 or j == 0 or i == m-1 or j == n-1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = 1
        
        result = 0
        while heap:
            height, i, j = heapq.heappop(heap)    
            for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    result += max(0, height-heightMap[x][y])
                    heapq.heappush(heap, (max(heightMap[x][y], height), x, y))
                    visited[x][y] = 1
        return result
