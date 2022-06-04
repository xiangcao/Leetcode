class Solution:
    # time: Let X = min(K, N), time is x + K LOg(X); 
    # space O(X) 
    def kthSmallest1(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        n = len(matrix)
        for r in range(min(k, n)):
            heap.append((matrix[r][0], r, 0))
        heapq.heapify(heap)
        
        while k:
            element, r, c = heapq.heappop(heap)
            if c < n-1:
                heapq.heappush(heap, (matrix[r][c+1], r, c+1))
            k -= 1
        return element

    def countLessEqual(self, matrix, mid, smaller, larger, x):
        count, n = 0, len(matrix)
        row, col = x - 1, 0

        while row >= 0 and col < x:
            if matrix[row][col] > mid:
               
                # As matrix[row][col] is bigger than the mid, let's keep track of the
                # smallest number greater than the mid
                larger = min(larger, matrix[row][col])
                row -= 1
                
            else:
                
                # As matrix[row][col] is less than or equal to the mid, let's keep track of the
                # biggest number less than or equal to the mid
                
                smaller = max(smaller, matrix[row][col])
                count += row + 1
                col += 1

        return count, smaller, larger
    # time N Log (Max - Min) 
    # space O(1)
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        n = len(matrix)
        start, end = matrix[0][0], matrix[n - 1][n - 1]
        x = min(k, n)
        while start < end:
            mid = start + (end - start) / 2
            smaller, larger = (matrix[0][0], matrix[n - 1][n - 1])

            count, smaller, larger = self.countLessEqual(matrix, mid, smaller, larger, x)

            if count == k:
                return smaller
            if count < k:
                start = larger  # search higher
            else:
                end = smaller  # search lower

        return start
