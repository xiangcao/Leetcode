class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        table = {}
        sum = 0 
        maxLen = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum == k:
                maxLen = i+1
            elif (sum - k) in table:
                    maxLen = max(maxLen, i-table[sum-k])
            if sum not in table:
                table[sum] = i
        return maxLen
                
            
