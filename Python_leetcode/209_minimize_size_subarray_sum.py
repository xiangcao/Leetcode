"""
https://leetcode.com/discuss/87685/template-subarray-substring-substring-repeating-characters
O(N) template for Minimum Size Subarray Sum & Minimum Window Substring & Longest Substring Without Repeating Characters

"""

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        sum = 0 
        start = end = 0
        minLen = len(nums) + 1
        while end < len(nums):
            sum += nums[end]
            end += 1
            while sum >= s:
                minLen = min(end-start, minLen)
                sum -= nums[start]
                start += 1
        if minLen <= len(nums):
            return minLen
        else:
            return 0
            

