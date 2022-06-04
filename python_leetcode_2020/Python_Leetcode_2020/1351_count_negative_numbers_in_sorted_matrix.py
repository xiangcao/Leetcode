"""
Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 

Return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
"""


This solution uses the fact that the negative regions of the matrix will form a "staircase" shape, e.g.:

++++++
++++--
++++--
+++---
+-----
+-----
What this solution then does is to "trace" the outline of the staircase.

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        r, c, cnt = m - 1, 0, 0
        while r >= 0 and c < n:
            if grid[r][c] < 0:
                cnt += n - c
                r -= 1
            else:
                c += 1
        return cnt
