"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        maxsofar = minsofar = nums[0]
        result = maxsofar
        
        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, curr * maxsofar, curr * minsofar)
            minsofar = min(curr, curr * maxsofar, curr * minsofar)
            maxsofar = temp_max
            result = max(result, maxsofar)
        return result
