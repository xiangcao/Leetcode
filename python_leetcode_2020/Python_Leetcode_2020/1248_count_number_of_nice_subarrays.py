"""
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

"""

class Solution(object):
    # Sliding window 
    # One Pass
    #Test case  [2,2,2,1,2,2,1,2,2,2] k = 2;  answer: 16
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i = count = res = 0
        A = nums
        for j in xrange(len(A)):
            if A[j] & 1:
                k -= 1
                count = 0
            while k == 0:
                k += A[i] & 1
                i += 1
                count += 1
            res += count
        return res

    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def atMost(k):
            res = i = 0
            for j in range(len(nums)):
                k -= A[j] % 2
                while k < 0:
                    k += A[i] % 2
                    i += 1
        def atMost(k):
            res = i = 0
            for j in xrange(len(A)):
                k -= A[j] % 2
                while k < 0:
                    k += A[i] % 2
                    i += 1
                res += j - i + 1
            return res

        return atMost(k) - atMost(k - 1)
