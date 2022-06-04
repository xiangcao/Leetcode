class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        totalCost = 0
        while len(sticks) > 1:
            cost = heapq.heappop(sticks) + heapq.heappop(sticks)
            
            totalCost += cost
            heapq.heappush(sticks, cost)
        
        return totalCost

