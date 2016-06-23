class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if not points:
            return True

        xList = [point[0] for point in points]
        minX = min(xList)
        maxX = max(xList)
        
        reflectX = (minX+maxX)/2.0
        
        table= collections.defaultdict(int)
        for point in points:
            table[(point[0], point[1])] += 1

        for point in points:
            if point[0] == reflectX:
                continue
            if (2*reflectX-point[0], point[1]) in table and (point[0], point[1]) in table:
                table[(2*reflectX-point[0], point[1])] -= 1
                table[(point[0], point[1])] -= 1
                continue
            else:
                return False
        return True
        
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if not points:
            return True

        xList = [point[0] for point in points]
        minX = min(xList)
        maxX = max(xList)
        
        reflectX = (minX+maxX)/2.0
        
        table= collections.defaultdict(int)
        for point in points:
            table[(point[0], point[1])] += 1

        for point in points:
            if point[0] == reflectX:
                continue
            if table[(2*reflectX-point[0], point[1])] == table[(point[0], point[1])]:
                table[(2*reflectX-point[0], point[1])] -= 1
                table[(point[0], point[1])] -= 1
                continue
            else:
                return False
        return True

    def isReflected(self, points):
        points.sort()
        return points == sorted([points[0][0] + points[-1][0] - x, y]
                            for x, y in points)

   
    def isReflected(self, points):
        if not points: return True
        X = min(points)[0] + max(points)[0]
        return {(x, y) for x, y in points} == {(X - x, y) for x, y in points}
