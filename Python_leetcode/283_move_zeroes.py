class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        source = target = 0
        
        for source in range(len(nums)):
            if nums[source] != 0:
                nums[target], nums[source] = nums[source], nums[target]
                target += 1
