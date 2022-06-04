"""
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)
"""
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist = lambda i: points[i][0]**2 + points[i][1] **2
 
        def sort(i, j, K):
            if i >= j:
                return
            k = random.randint(i, j)
            points[i], points[k] = points[k], points[i]

            mid = partition(i, j)
            if K < mid - i + 1:
                sort(i, mid - 1, K)
            elif K > mid - i + 1:
                sort(mid + 1, j, K - (mid - i + 1))

        def partition(i, j):
            oi = i
            di = dist(i)
            i += 1
            while True:
                while i < j and dist(i) < di:
                    i += 1
                while i <= j and dist(j) >= di:
                    j -= 1
                if i >= j:
                    break
                points[i], points[j] = points[j], points[i]    
            points[oi], points[j] = points[j], points[oi]
            return j

        sort(0, len(points)-1, K)
        return points[:K]

# heap:
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        def getDistance(point):
            return math.sqrt(pow(point[0],2) + pow(point[1], 2))
        for i in range(min(K, len(points))):
            heapq.heappush(heap, (-getDistance(points[i]), i) )
        for i in range(K, len(points)):
            curDistance = getDistance(points[i])
            if curDistance < -heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (-curDistance, i))

        return [points[value[1]] for _, value in enumerate(heap)]
