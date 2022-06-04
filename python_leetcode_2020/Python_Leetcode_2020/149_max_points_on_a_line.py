"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

"""

class Solution:
    # Note: in python3, math.gcd() is available; and math.gcd(0,-1) is 1
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points: return 0
        if len(points) <= 2:
            return len(points)

        solution = 0
        for i in range(len(points)):
            localmap = collections.defaultdict(lambda: 1)
            duplicate = 0
            localmax = 0
            for j in range(i+1, len(points)):
                deltaX = points[j][0] - points[i][0]
                deltaY = points[j][1] - points[i][1]
                if (deltaX == 0 and deltaY == 0):
                    duplicate+=1
                    continue
                # vertical lines
                if deltaX == 0:
                    dX, dY = 0, 0
                else:
                    # to have a consistent representation,
                    # keep the delta_x always positive
                    if deltaX < 0:
                        deltaX, deltaY = -deltaX, -deltaY
                    divisor = math.gcd(deltaX, deltaY)

                    dX = deltaX / divisor
                    dY = deltaY / divisor

                key = str(dX) + "," + str(dY)
                localmap[key] += 1
                localmax = max(localmax, localmap[key])
            localmax = max(1, localmax)
            solution = max(solution, duplicate + localmax)
        
        return solution


