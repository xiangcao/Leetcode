"""
Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        def _rob(nums):
            total0, total1 = 0, 0
            for i in nums:
                total0, total1 = max(total0, total1), total0+i
            return max(total0, total1)
        return max(_rob(nums[1:]), _rob(nums[:-1]))
        
#http://bookshadow.com/weblog/2015/05/20/leetcode-house-robber-ii/ 
#http://blog.csdn.net/kangrydotnet/article/details/45921887   不同的解法
