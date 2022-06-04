"""
Given a set of points in the xy-plane, determine the minimum area of any rectangle formed from these points, with sides not necessarily parallel to the x and y axes.

If there isn't any rectangle, return 0.
"""

class Solution(object):
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        res = float("inf")
        if (len(points) < 4): return 0.0
        centerToPointsMap = collections.defaultdict(list)

        def dist(i, j):
            x_dist = points[i][0] - points[j][0]
            y_dist = points[i][1] - points[j][1]
            return math.sqrt(x_dist* x_dist + y_dist * y_dist)

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                distance = dist(i, j)
                x_center = (points[i][0] + points[j][0]) / 2.0
                y_center = (points[i][1] + points[j][1]) / 2.0
                key = str(distance)+"+"+str(x_center)+"+"+str(y_center)
                centerToPointsMap[key].append((i, j))
        
        for group in centerToPointsMap.values():
            for i in range(len(group)):
                for j in range(i+1, len(group)):
                    p1 = group[i][0]
                    p2 = group[i][1]
                    p3 = group[j][0]
                    # p4 = group[j][1]
                    
                    res = min(res, dist(p1, p3) * dist(p2, p3))
 
        return res if res < float("inf") else 0
