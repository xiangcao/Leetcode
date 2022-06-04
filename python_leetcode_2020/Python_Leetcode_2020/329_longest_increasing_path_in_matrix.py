"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).
"""
# solution 1
Approach #1 (Naive DFS) [Time Limit Exceeded]

Intuition

DFS can find the longest increasing path starting from any cell. We can do this for all the cells.

Algorithm

Each cell can be seen as a vertex in a graph G. If two adjacent cells have value  a<b, i.e. increasing then we have a directed edge (a,b). The problem then becomes:
      Search the longest path in the directed graph G
Naively, we can use DFS or BFS to visit all the cells connected starting from a root. We update the maximum length of the path during search and find the answer when it finished.

Usually, in DFS or BFS, we can employ a set visited to prevent the cells from duplicate visits. We will introduce a better algorithm based on this in the next section.
// Naive DFS Solution
// Time Limit Exceeded
Time O(2^(m+n);  The search is repeated for each valid increasing path. In the worst case we can have O(2^{m+n}) calls
Space O(mn);   for each DFS, we need O(h) spaces used by the stack, O(h) = O(mn) in worse case
public class Solution {
  private static final int[][] dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
  private int m, n;

  public int longestIncreasingPath(int[][] matrix) {
      if (matrix.length == 0) return 0;
      m = matrix.length;
      n = matrix[0].length;
      int ans = 0;
      for (int i = 0; i < m; ++i)
          for (int j = 0; j < n; ++j)
              ans = Math.max(ans, dfs(matrix, i, j));
      return ans;
  }

  private int dfs(int[][] matrix, int i, int j) {
      int ans = 0;
      for (int[] d : dirs) {
          int x = i + d[0], y = j + d[1];
          if (0 <= x && x < m && 0 <= y && y < n && matrix[x][y] > matrix[i][j])
              ans = Math.max(ans, dfs(matrix, x, y));
      }
      return ++ans;
  }
}

# solution 2
// DFS + Memoization Solution
// Accepted and Recommended
Time complexity : O(mn). Each vertex/cell will be calculated once and only once, and each edge will be visited once and only once. The total time complexity is then O(V+E). V is the total number of vertices and E is the total number of edges. In our problem, O(V) = O(mn), O(E) = O(4V) = O(mn).
Space complexity : O(mn). The cache dominates the space complexity.
public class Solution {
    private static final int[][] dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    private int m, n;

    public int longestIncreasingPath(int[][] matrix) {
        if (matrix.length == 0) return 0;
        m = matrix.length; n = matrix[0].length;
        int[][] cache = new int[m][n];
        int ans = 0;
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                ans = Math.max(ans, dfs(matrix, i, j, cache));
        return ans;
    }

    private int dfs(int[][] matrix, int i, int j, int[][] cache) {
        if (cache[i][j] != 0) return cache[i][j];
        for (int[] d : dirs) {
            int x = i + d[0], y = j + d[1];
            if (0 <= x && x < m && 0 <= y && y < n && matrix[x][y] > matrix[i][j])
                cache[i][j] = Math.max(cache[i][j], dfs(matrix, x, y, cache));
        }
        return ++cache[i][j];
    }
}


#
Approach #3 (Peeling Onion) [Accepted]: use topological sort, and count layers of topological sorting
Intuition

The result of each cell only related to the result of its neighbors. Can we use dynamic programming?

Algorithm

If we define the longest increasing path starting from cell (i, j) as a function f(i, j)

then we have the following transition function

f(i,j)=max{f(x,y)∣(x,y) is a neighbor of(i,j) and matrix[x][y]>matrix[i][j]}+1

This formula is the same as used in the previous approaches. With such transition function, one may think that it is possible to use dynamic programming to deduce all the results without employing DFS!

That is right with one thing missing: we don't have the dependency list.

For dynamic programming to work, if problem B depends on the result of problem A, then we must make sure that problem A is calculated before problem B. Such order is natural and obvious for many problems. For example the famous Fibonacci sequence:

F(0) = 1, F(1) = 1, F(n) = F(n - 1) + F(n - 2)

The subproblem F(n) depends on its two predecessors. Therefore, the natural order from 0 to n is the correct order. The dependent is always behind the dependee.

The terminology of such dependency order is "Topological order" or "Topological sorting":

Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge (u, v), vertex u comes before v in the ordering.

In our problem, the topological order is not natural. Without the value in the matrix, we couldn't know the dependency relation of any two neighbors A and B. We have to perform the topological sort explicitly as a preprocess. After that, we can solve the problem dynamically using our transition function following the stored topological order.

There are several ways to perform the topological sorting. Here we employ one of them called "Peeling Onion".

The idea is that in a DAG, we will have some vertex who doesn't depend on others which we call "leaves". We put these leaves in a list (their internal ordering does matter), and then we remove them from the DAG. After the removal, there will be new leaves. We do the same repeatedly as if we are peeling an onion layer by layer. In the end, the list will have a valid topological ordering of our vertices.

In out problem, since we want the longest path in the DAG, which equals to the total number of layers of the "onion". Thus, we can count the number of layers during "peeling" and return the counts in the end without invoking dynamic programming.
Time complexity : O(mn). The the topological sort is O(V+E) = O(mn). Here, V is the total number of vertices and E is the total number of edges. In our problem, O(V)=O(mn), O(E) = O(4V) = O(mn).

Space complexity : O(mn)  We need to store the out degrees and each level of leaves.

// Topological Sort Based Solution
// An Alternative Solution
public class Solution {
    private static final int[][] dir = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    private int m, n;
    public int longestIncreasingPath(int[][] grid) {
        int m = grid.length;
        if (m == 0) return 0;
        int n = grid[0].length;
        // padding the matrix with zero as boundaries
        // assuming all positive integer, otherwise use INT_MIN as boundaries
        int[][] matrix = new int[m + 2][n + 2];
        for (int i = 0; i < m; ++i)
            System.arraycopy(grid[i], 0, matrix[i + 1], 1, n);

        // calculate outdegrees
        int[][] outdegree = new int[m + 2][n + 2];
        for (int i = 1; i <= m; ++i)
            for (int j = 1; j <= n; ++j)
                for (int[] d: dir)
                    if (matrix[i][j] < matrix[i + d[0]][j + d[1]])
                        outdegree[i][j]++;

        // find leaves who have zero out degree as the initial level
        n += 2;
        m += 2;
        List<int[]> leaves = new ArrayList<>();
        for (int i = 1; i < m - 1; ++i)
            for (int j = 1; j < n - 1; ++j)
                if (outdegree[i][j] == 0) leaves.add(new int[]{i, j});

        // remove leaves level by level in topological order
        int height = 0;
        while (!leaves.isEmpty()) {
            height++;
            List<int[]> newLeaves = new ArrayList<>();
            for (int[] node : leaves) {
                for (int[] d:dir) {
                    int x = node[0] + d[0], y = node[1] + d[1];
                    if (matrix[node[0]][node[1]] > matrix[x][y])
                        if (--outdegree[x][y] == 0)
                            newLeaves.add(new int[]{x, y});
                }
            }
            leaves = newLeaves;
        }
        return height;
    }
} 
Remarks
Memoization: for a problem with massive duplicate calls, cache the results.
Dynamic programming requires the subproblem solved in topological order. In many problems, it coincides the natural order. For those who doesn't, one need perform topological sorting first. Therefore, for those problems with complex topology (like this one), search with memorization is usually an easier and better choice.

# python code for solution 2 above
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        m, n = len(matrix),len(matrix[0])
        cache = [[0] * n for _ in range(m)]
        maxDist = 1

        def neighbor(i, j):
            for dx, dy in [(0,1), (0,-1), (1,0), (-1, 0)]:
                yield i + dx, j + dy

        def dfs(i, j):
            if cache[i][j] != 0:
                return cache[i][j]
            localmax = 1
            for nextx, nexty in neighbor(i, j):
                if m > nextx >= 0 and n > nexty >= 0 and matrix[nextx][nexty] > matrix[i][j]:
                    localmax = max(localmax, 1 + dfs(nextx, nexty))
            cache[i][j] = localmax
            return localmax

        for i in range(m):
            for j in range(n):
                maxDist = max(maxDist, dfs(i, j))
        return maxDist
            
