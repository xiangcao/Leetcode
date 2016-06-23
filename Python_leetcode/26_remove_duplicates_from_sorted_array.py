class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0 
        prev = None
        for i in range(len(nums)):
            if nums[i] != prev:
                prev, nums[k] = nums[i], nums[i]
                k += 1
        return k

#秒过
