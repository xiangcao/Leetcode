"""
75. Sort Colors
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with an one-pass algorithm using only constant space?
"""
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        begin, end = 0, len(nums)-1
        i = 0
        while i < len(nums) and begin < end:
            if nums[i] == 0:
                if i > begin:
                    nums[begin], nums[i] = nums[i], nums[begin]
                else:
                    i += 1
                begin += 1
            elif nums[i] == 2:
                if i < end:
                    nums[end], nums[i] = nums[i], nums[end]
                else:
                    i += 1
                end -= 1
            else:
                i += 1

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        begin, end = 0, len(nums)-1
        i = 0
        while i < len(nums) and begin < end:
            if nums[i] == 0:
                if i > begin:
                    if nums[begin] != 0:
                        nums[begin], nums[i] = nums[i], nums[begin]
                else:
                    i += 1  
                begin += 1
            elif nums[i] == 2:
                if i < end:
                    if nums[end] != 2:
                        nums[end], nums[i] = nums[i], nums[end]
                else:
                    i += 1
                end -= 1
            else:
                i += 1
