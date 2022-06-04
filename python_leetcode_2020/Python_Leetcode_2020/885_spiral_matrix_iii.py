"""
On a 2 dimensional grid with R rows and C columns, we start at (r0, c0) facing east.

Here, the north-west corner of the grid is at the first row and column, and the south-east corner of the grid is at the last row and column.

Now, we walk in a clockwise spiral shape to visit every position in this grid. 

Whenever we would move outside the boundary of the grid, we continue our walk outside the grid (but may return to the grid boundary later.) 

Eventually, we reach all R * C spaces of the grid.

Return a list of coordinates representing the positions of the grid in the order they were visited.
"""
class Solution:
    # similar walk as 54 spiral matrix and 59 spiral matrix II
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        m = R
        n = C
        L, R, T, B = c0-1, c0+1, r0, r0+1
        dir = 0
        result=[]
        layer = 0
        while True:
            if (dir == 0):
                for k in range(L+1, R+1):
                    if 0 <= T < m and 0 <= k < n:
                        result.append((T,k))
                if layer > 0:
                    L -= 1
                dir += 1
            elif dir == 1:
                for k in range(T+1, B+1):
                    if 0 <= k < m and 0 <= R < n:
                        result.append((k, R))
                    
                T -= 1
                dir += 1
            elif dir == 2:
                for k in range(R-1, L-1, -1):
                    if 0 <= B < m and 0 <= k < n:
                        result.append((B, k))
                R += 1
                dir += 1
            else:
                for k in range(B-1, T-1, -1):
                    if 0 <= k < m and 0 <= L < n:
                        result.append((k, L))
                B += 1
                dir = 0
            layer += 1
            if len(result) == m * n:
                break
        return result

    def spiralMatrixIII(self, R, C, r0, c0):
        ans = [(r0, c0)]
        if R * C == 1: return ans

        # For walk length k = 1, 3, 5 ...
        for k in range(1, 2*(R+C), 2):
            # For direction (dr, dc) = east, south, west, north;
            # and walk length dk...
            for dr, dc, dk in ((0, 1, k), (1, 0, k), (0, -1, k+1), (-1, 0, k+1)):
                # For each of dk units in the current direction ...
                for _ in range(dk):

                    # Step in that direction
                    r0 += dr
                    c0 += dc

                    # If on the grid ...
                    if 0 <= r0 < R and 0 <= c0 < C:
                        ans.append((r0, c0))
                        if len(ans) == R * C:
                            return ans


