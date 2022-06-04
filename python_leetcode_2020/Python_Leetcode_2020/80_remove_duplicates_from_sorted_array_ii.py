"""
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = 0, 0
        count = 1
        while fast < len(nums):
            if fast > 0:
                if nums[fast] == nums[fast-1]:
                    count += 1
                else:
                    count = 1

            if count <= 2:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
