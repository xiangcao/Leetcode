class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        if not (nums1 and nums2):
            return []
        for i in range(min(k,len(nums1))):
            heapq.heappush(heap, (nums1[i]+nums2[0], i, 0))
        result=[]
        while heap and k > 0:
            _, i, j = heapq.heappop(heap)
            k -= 1
            result.append([nums1[i], nums2[j]])
            if j < len(nums2)-1:
                heapq.heappush(heap, (nums1[i]+nums2[j+1], i, j+1))
        return result
