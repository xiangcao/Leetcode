class Solution1:
    # 88 ms
    def findCheapestPrice1(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(collections.defaultdict)
        for source, dest, price in flights:
            graph[source][dest] = price

        costs = [float('inf') for _ in range(n)]
        stops = [float('inf') for _ in range(n)]
        costs[src], stops[src] = 0, 0

        minHeap = [(0, 0, src)]

        while minHeap:
            cost, stop, node = heapq.heappop(minHeap)
            if node == dst:
                return cost
            if stop == K + 1:
                continue
            for nei in graph[node]:
                neighbor_cost = graph[node][nei]
                if cost + neighbor_cost < costs[nei]:
                    costs[nei] = cost + neighbor_cost
                    heapq.heappush(minHeap, (costs[nei], stop+1, nei))
                elif stop < stops[nei]:
                    # stops[nei] = stop
                    heapq.heappush(minHeap, (cost + neighbor_cost, stop+1, nei))
        return -1 if costs[dst] == float("inf") else costs[dst]

    # 88 ms
    def findCheapestPrice2(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        f = collections.defaultdict(dict)
        for a, b, p in flights:
            f[a][b] = p
        heap = [(0, src, K + 1)]
        while heap:
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            if k > 0:
                for j in f[i]:
                    heapq.heappush(heap, (p + f[i][j], j, k - 1))
        return -1

    # BFS  1080 ms
    # Time: O(E*K);  Space: O(V^2 + V*K)
    def findCheapestPrice3(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        # Build the adjacency matrix
        adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
        for s, d, w in flights:
            adj_matrix[s][d] = w
            
        # Shortest distances dictionary
        distances = {}
        distances[(src, 0)] = 0
        
        # BFS Queue
        bfsQ = deque([src])
        
        # Number of stops remaining
        stops = 0
        ans = float("inf")
        
        # Iterate until we exhaust K+1 levels or the queue gets empty
        while bfsQ and stops < K + 1:
            
            # Iterate on current level
            length = len(bfsQ)
            for _ in range(length):
                node = bfsQ.popleft()
                
                # Loop over neighbors of popped node
                for nei in range(n):
                    if adj_matrix[node][nei] > 0:
                        dU = distances.get((node, stops), float("inf"))
                        dV = distances.get((nei, stops + 1), float("inf"))
                        wUV = adj_matrix[node][nei]
                        
                        # No need to update the minimum cost if we have already exhausted our K stops. 
                        if stops == K and nei != dst:
                            continue
                        
                        if dU + wUV < dV:
                            distances[nei, stops + 1] = dU + wUV
                            bfsQ.append(nei)
                            
                            # Shortest distance of the destination from the source
                            if nei == dst:
                                ans = min(ans, dU + wUV)
            stops += 1   
        
        return -1 if ans == float("inf") else ans

    # 148 ms  Bellman-Ford; Time O(K*E); Space O(V)
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        # We use two arrays for storing distances and keep swapping
        # between them to save on the memory
        distances = [[float('inf')] * n for _ in range(2)]
        distances[0][src] = distances[1][src] = 0
        
        # K + 1 iterations of Bellman Ford
        for iterations in range(K + 1):

            # Iterate over all the edges
            for s, d, wUV in flights:
   
                # Current distance of node "s" from src
                dU = distances[1 - iterations&1][s]
                
                # Current distance of node "d" from src
                # Note that this will port existing values as
                # well from the "previous" array if they didn't already exist
                dV = distances[iterations&1][d]
                
                # Relax the edge if possible
                if dU + wUV < dV:
                    distances[iterations&1][d] = dU + wUV
                    
        return -1 if distances[K&1][dst] == float("inf") else distances[K&1][dst]


# DFS with memoization;  332 ms
"""
Time Complexity: The time complexity for a recursive solution is defined by the number of recursive calls we make and the time it takes to process one recursive call. The number of recursive calls we can potentially make is O(V⋅K). In each recursive call, we iterate over a given node's neighbors. That takes time O(V) because we are using an adjacency matrix. Thus, the overall time complexity is 
O(V^2⋅K).
Space Complexity: O(VK + V^2) where O(VK) is occupied by the memo dictionary and the rest by the adjacency matrix structure we build in the beginning

class Solution:
    def __init__(self):
        self.adj_matrix = None
        self.memo = {}
    
    def findShortest(self, node, stops, dst, n):
        # No need to go any further if the destination is reached    
        if node == dst:
            return 0
        
        # Can't go any further if no stops left
        if stops < 0:
            return float("inf")
        
        # If the result of this state is already cached, return it
        if (node, stops) in self.memo:
            return self.memo[(node, stops)]
        
        # Recursive calls over all the neighbors
        ans = float("inf")
        for neighbor in range(n):
            if self.adj_matrix[node][neighbor] > 0:
                ans = min(ans, self.findShortest(neighbor, stops-1, dst, n) + self.adj_matrix[node][neighbor])
        
        # Cache the result
        self.memo[(node, stops)] = ans        
        return ans
    
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        self.adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
        self.memo = {}
        for s, d, w in flights:
            self.adj_matrix[s][d] = w
        
        result = self.findShortest(src, K, dst, n)
        return -1 if result == float("inf") else result


C++ DFS 60 ms
class Solution {
public:
  int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int K) {
    g_.clear();  
    for (const auto& e : flights)
      g_[e[0]].emplace_back(e[1], e[2]);
    vector<int> visited(n, 0);
    visited[src] = 1;
    int ans = INT_MAX;
    dfs(src, dst, K + 1, 0, visited, ans);
    return ans == INT_MAX ? - 1 : ans;
  }
private:
  unordered_map<int, vector<pair<int,int>>> g_;
  
  void dfs(int src, int dst, int k, int cost, vector<int>& visited, int& ans) {
    if (src == dst) {
      ans = cost;
      return;
    }
    
    if (k == 0) return;    
    
    for (const auto& p : g_[src]) {
      if (visited[p.first]) continue; // do not visit the same city twice.
      if (cost + p.second > ans) continue; // IMPORTANT!!! prunning 
      visited[p.first] = 1;
      dfs(p.first, dst, k - 1, cost + p.second, visited, ans);
      visited[p.first] = 0;
    }
  }
};

