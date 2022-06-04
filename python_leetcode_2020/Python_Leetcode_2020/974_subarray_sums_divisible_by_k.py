Same as leetcode 560 Subarray Sum Equals K
Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.

 

Example 1:

Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]


class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        counter = [0] * K
        counter[0] = 1
        
        presum = 0
        totalCount = 0
        for e in A:
            presum += e
            presum %= K
            totalCount += counter[presum]
            counter[presum] += 1

        return totalCount
        #return sum(count * (count-1) / 2 for count in counter if count > 0)
