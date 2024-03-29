"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
"""

class Solution(object):
    def minSubArrayLen(self, s, nums): 
        # time exceeded
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        minSize = len(nums) + 1
        for i in range(len(nums)):
            totalSum = 0
            for j in range(i, len(nums)):
                totalSum += nums[j]
                if totalSum >= s:
                    minSize = min(minSize, j-i+1)
                    break
        return minSize if minSize != len(nums)+1 else 0

    # Sliding Window
    def minSubArrayLen2(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, 0
        total = 0
        n = len(nums)
        minsize = n + 1
        while right < n:
            total += nums[right]
            while total >= s:
                minsize = min(minsize, right - left + 1)
                total -= nums[left]
                left += 1
            right += 1
        return minsize if minsize != len(nums) + 1 else 0
