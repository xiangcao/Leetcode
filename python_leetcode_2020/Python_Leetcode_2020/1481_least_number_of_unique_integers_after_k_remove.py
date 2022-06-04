"""
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

Constraints:

1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length
"""

class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        hp = [val for key, val in collections.Counter(arr).items()]
        heapq.heapify(hp)
        while k > 0:
            k -= heapq.heappop(hp)
        return len(hp) + (k < 0)
    
    def findLeastNumOfUniqueInts(self, arr, k):
        c = Counter(arr)
        
        cnt, remaining = Counter(c.values()), len(c)
        for key in range(1, len(arr) + 1): 
            # there are cnt[key] different integers that occurs key times
            if k >= key * cnt[key]:
                k -= key * cnt[key]
                remaining -= cnt[key]
            else:
                return remaining - k // key
        return remaining


