"""
Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.
"""

class Solution(object):
    # 1904 ms O(N^2)
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        """
        Intuition

For each pair of points in the array, consider them to be the long diagonal of a potential rectangle. We can check if all 4 points are there using a Set.

For example, if the points are (1, 1) and (5, 5), we check if we also have (1, 5) and (5, 1). If we do, we have a candidate rectangle.

Algorithm

Put all the points in a set. For each pair of points, if the associated rectangle are 4 distinct points all in the set, then take the area of this rectangle as a candidate answer.
"""
        S = set(map(tuple, points))
        ans = float('inf')
        for j, p2 in enumerate(points):
            for i in xrange(j):
                p1 = points[i]
                if (p1[0] != p2[0] and p1[1] != p2[1] and
                        (p1[0], p2[1]) in S and (p2[0], p1[1]) in S):
                    ans = min(ans, abs(p2[0] - p1[0]) * abs(p2[1] - p1[1]))
        return ans if ans < float('inf') else 0

    # 1200 ms
    def minAreaRect(self, points):
        seen = set()
        res = float('inf')
        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    area = abs(x1 - x2) * abs(y1 - y2)
                    if area and area < res:
                        res = area
            seen.add((x1, y1))
        return res if res < float('inf') else 0
    
    # 164 ms; sort by column
    def minAreaRect(self, points):
        n = len(points)
        nx = len(set(x for x, y in points))
        ny = len(set(y for x, y in points))
        if nx == n or ny == n:
            return 0

        p = collections.defaultdict(list)
        if nx > ny:
            for x, y in points:
                p[x].append(y)
        else:
            for x, y in points:
                p[y].append(x)

        lastx = {}
        res = float('inf')
        for x in sorted(p):
            p[x].sort()
            for i in range(len(p[x])):
                for j in range(i):
                    y1, y2 = p[x][j], p[x][i]
                    if (y1, y2) in lastx:
                        res = min(res, (x - lastx[y1, y2]) * abs(y2 - y1))
                    lastx[y1, y2] = x
        return res if res < float('inf') else 0
