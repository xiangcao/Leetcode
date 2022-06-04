"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
"""
class Solution(object):
    #Recursive with Memo
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        memo = [-1] * len(nums)
        memo[0] = nums[0]
        def helper(i):
            if i < 0:
                return 0
            if memo[i] >= 0:
                return memo[i]
            memo[i] = max(helper(i-2) + nums[i], helper(i-1))
            return memo[i]
        return helper(len(nums)-1)

    # One dimension DP Bottom Up 
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0 
        memo = [-1] * (len(nums)+ 1)
        memo[0] = 0
        memo[1] = nums[0]
        
        for i in range(2, len(nums) + 1):
            memo[i] = max(memo[i-2] + nums[i-1], memo[i-1])
        return memo[-1]
    
    # Two variables DP Bottom up
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        prev = 0
        cur = nums[0]
        for i in range(1, len(nums)):
            temp = cur
            cur = max(prev + nums[i], cur)
            prev = temp
        return cur
