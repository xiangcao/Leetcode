"""
Given an array of integers nums and an integer target.

Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.


two sum approach: 
Explanation
Sort input A first,
For each A[i], find out the maximum A[j]
that A[i] + A[j] <= target.

For each elements in the subarray A[i+1] ~ A[j],
we can pick or not pick,
so there are 2 ^ (j - i) subsequences in total.
So we can update res = (res + 2 ^ (j - i)) % mod.

We don't care the original elements order,
we only want to know the count of sub sequence.
So we can sort the original A, and the result won't change.


Complexity
Time O(NlogN)
Space O(1) for python
(O(N) space for java and c++ can be save anyway)
"""
class Solution:
    #O(NLogN) sorting, then O(N) for counting; accepted
    def numSubseq(self, A, target):
        A.sort()
        l, r = 0, len(A) - 1
        res = 0
        mod = 10**9 + 7
        while l <= r:
            if A[l] + A[r] > target:
                r -= 1
            else:
                res += pow(2, r - l, mod)
                l += 1
        return res % mod
    
    #Time exceeded O(N^2)
    def numSubseq2(self, nums: List[int], target: int) -> int:
        nums.sort()
        i = 0
        j = 0
        result = 0
        while j < len(nums):
            if nums[j] + nums[i] <= target:
                j += 1
                if j >= len(nums):
                    result += pow(2, j-i-1)
                    i += 1
                    j = i
            elif j > i:
                result += pow(2, j-i-1)
                i += 1
                j = i
            else:
                break
        # all subsuequence from [0, j)
        return result % (pow(10,9) + 7)
            
                
            
