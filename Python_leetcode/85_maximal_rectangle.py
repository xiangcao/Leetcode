class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def getMaxArea(heightArray):
            stack=[]
            heightArray.append(0)
            maxArea = 0
            i = 0
            while  i < len(heightArray):
                if len(stack) == 0 or heightArray[stack[-1]] < heightArray[i]:
                    stack.append(i)
                    i += 1
                else:
                    x = stack.pop()
                    if len(stack) == 0:
                        width = i
                    else:
                        width = i - stack[-1] - 1
                    area = width * heightArray[x]
                    maxArea = max(area, maxArea)
            return maxArea

        maxRow = len(matrix)
        if maxRow == 0:
            return 0
        maxCol = len(matrix[0])
        
        #Solution 1, accepted
        height = [ [0] * maxCol ] * maxRow
        maxArea = 0
        for i in range(maxRow):
            for j in range(maxCol):
                if i == 0:
                    height[i][j] = 0 if matrix[i][j] == "0" else 1
                else:
                    height[i][j] = 0 if matrix[i][j] == "0" else height[i-1][j]+1
            maxArea = max(maxArea, getMaxArea(height[i]))

        #solution 2 ACCEPTED
        height2 = [ [0] * maxCol ] * maxRow
        maxArea = 0
        for i in range(maxRow):
            for j in range(maxCol):
                if matrix[i][j] == "1":
                    height2[i][j] = 1 if i == 0 else height2[i-1][j]+1
                else:
                    height2[i][j] = 0
            maxArea = max(maxArea, getMaxArea(height2[i]))

        return maxArea

sol = Solution()
matrix=[["0","1"],["1","0"]]
#matrix=[["0", "1", "1"], ["1","1","0"],["0", "1","1"]]
print "max rectangle is ", sol.maximalRectangle(matrix)
