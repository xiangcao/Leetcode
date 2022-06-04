"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6

"""

# Runtime: 200 ms, faster than 95.96% of Python3 online submissions for Maximal Rectangle.
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def maxRectangle(heights):
            heights.append(0)
            stack = [-1]
            
            maxarea = 0 
            for i in range(len(heights)):
                while heights[i] < heights[stack[-1]]:
                    maxarea = max(maxarea, heights[stack.pop()] * (i - stack[-1]-1))
                stack.append(i)
            heights.pop()
            return maxarea
        if not matrix: return 0
        dp = [0] * len(matrix[0])
        maxarea = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0
            maxarea = max(maxarea, maxRectangle(dp))
        return maxarea
