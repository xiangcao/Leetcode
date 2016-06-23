# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if not points or len(points) == 0:
            return 0
        
        def getSlope(pointA, pointB):
            if pointA.x == pointB.x:
                return 'inf'
            else:
                return 1.0 * (pointB.y - pointA.y)/(pointB.x-pointA.x)

        maxPoints = 1
        for i in range(len(points)):
            table= collections.defaultdict(lambda:0)
            table['inf']=0
            duplicate = 1
            for j in range(i+1, len(points)):
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    duplicate += 1
                    continue
                slope = getSlope(points[i], points[j])
                table[slope] += 1
            maxPoints = max(maxPoints, max(table.values())+duplicate)
        return maxPoints
