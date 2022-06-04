"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        missing = 0

        # Using XOR, "add" each number in 0 ... n that "should be" in the list
        for i in range(n + 1):
            missing ^= i

        # Using XOR, "subtract" each number that we actually find in the list
        for num in nums:
            missing ^= num

        # We've removed every number except the missing value, so this must be it
        return missing
