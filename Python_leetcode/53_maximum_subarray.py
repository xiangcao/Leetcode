class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = nums[0]
        sum = 0 
        for i in nums:
            sum += i
            maxSum = max(maxSum, sum)
            if sum < 0:
                sum = 0 
        return maxSum
        #testcase [-2 -1]
        #testcase [-2]
        
