"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram. 
"""

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack=[]
        
        i = 0
        maxArea = 0
        heights.append(0)
        while i < len(heights):
            if len(stack) == 0 or heights[i] > heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                k = stack.pop()
                if len(stack) == 0:
                    preBoundary = -1
                else:
                    preBoundary = stack[-1]
                area = heights[k] * (i - preBoundary - 1)
                maxArea = max(area, maxArea)

        return maxArea


sol = Solution()
heights=[4,2]
sol.largestRectangleArea(heights)
