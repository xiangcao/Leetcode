"""
You are given an m * n matrix, mat, and an integer k, which has its rows sorted in non-decreasing order.

You are allowed to choose exactly 1 element from each row to form an array. Return the Kth smallest array sum among all possible arrays.

Idea: To understand this problem, first please look at - 373. Find K Pairs with Smallest Sums. The function kSmallestPairs can be taken directly from Problem - 373. So we start merging two rows at a time by using the function kSmallestPairs, m-1 times, keeping each time the size of the res at most k = 200.

The time complexity of kSmallestPairs each time it is called is k * logk. Since it is called m-1 times, so we have total time complexity = k * logk * (m-1).

Note: k * logk * (m-1) <= 200 * log(200) * 40.

Time : O(k * logk * (m-1)).
Space : O(200).
"""
class Solution:

    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m, n = len(mat), len(mat[0])
        ret = mat[0]
        for i in range(1, m):
            ret = self.kSmallestPairs(ret, mat[i], k)
        return ret[-1]
    
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
            result.append(nums1[i] + nums2[j])
            if j < len(nums2)-1:
                heapq.heappush(heap, (nums1[i]+nums2[j+1], i, j+1))
        return result
