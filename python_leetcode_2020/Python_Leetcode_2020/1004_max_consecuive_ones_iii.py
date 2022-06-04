"""
Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s. 
"""
# sliding window
class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        ans = 0
        zero = 0
        l, r = 0, 0
        for r in range(len(A)):
            if (A[r] == 0) :                         
                zero += 1
            while (zero > K):
                if (A[l] == 0):
                    zero -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans            
