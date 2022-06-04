class Solution(object):
    # Number of unique distances should be 2. (4 for sides, and 2 for diagonals)
    def validSquare1(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        points = [p1, p2, p3, p4]
        
        dists = collections.Counter()
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dists[self.getDistance(points[i], points[j])] += 1
        
        return len(dists.values())==2 and 4 in dists.values() and 2 in dists.values()
        
    def getDistance(self, p1, p2):
        return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2


    """
    Only three possible cases after sorting the given set of points based on x-coordincate values; and in case of a tie, based on their y-coordinate values.
    In each case, after sorting, we obtain the following conclusion regarding the connections of the points:
    1. p0p1, p1p3, p3p2, p2p0 form the four sides of any possible valid square
    2. p0p3 and p1p2 form the diagonals of the square
    """
    def validSquare(self, p1, p2, p3, p4):
        def getDistance(p1, p2):
            return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
        p = [p1, p2, p3, p4]
        p.sort()
        return getDistance(p[0], p[1]) and getDistance(p[0], p[1]) == getDistance(p[1], p[3]) and getDistance(p[1], p[3]) == getDistance(p[3], p[2]) and getDistance(p[3], p[2]) == getDistance(p[2], p[0])  and getDistance(p[0],p[3])==getDistance(p[1],p[2]);
