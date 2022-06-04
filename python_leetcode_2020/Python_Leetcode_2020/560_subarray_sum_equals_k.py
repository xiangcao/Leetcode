"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2
 

Constraints:

The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

class Solution(object):
    def subarraySum(self, nums, k):
        counter = collections.Counter()
        counter[0] = 1
        
        presum = 0
        totalCount = 0
        for e in nums:
            presum += e
            totalCount += counter[presum - k]
            counter[presum] += 1

        return totalCount

Failure:
nums: [1]
k: 0
output: 1
Expected: 0

[-1,-1,1]
0
Output 0
Expected 1


class Solution:
    #[1,1,1], 2 => 2
    #[1,-1, 2, -2], 0 => 3
    #[1,2,3], 3 = > 2
    #[1,2,3,1]  6 => 2
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = collections.defaultdict(int)
        prefixSum[0] = 1
        curSum = 0
        result = 0
        for n in nums:
            curSum += n
            result += prefixSum[curSum - k]
            prefixSum[curSum] += 1
        return result
