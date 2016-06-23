class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 1
        #minimum = max(min(nums), 1)
        minimum = 1
        i = 0 
        while i< len(nums):
            targetIndex = nums[i] - minimum
            if targetIndex < 0 or targetIndex >= len(nums) or nums[targetIndex] == nums[i]:
                i += 1
                continue
            nums[targetIndex], nums[i] = nums[i], nums[targetIndex]
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return nums[-1] + 1
                
       
