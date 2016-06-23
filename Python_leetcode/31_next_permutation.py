class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lens = len(nums)
        if lens <= 1:
            return
        left = -1
        for i in reversed(range(lens-1)):
            if nums[i] < nums[i+1]:
                left = i 
                break
        if left == -1:
            nums[:] = nums[::-1]
        for i in reversed(range(lens)):
            if nums[i] > nums[left]:
                nums[left], nums[i] = nums[i], nums[left]
                break
        nums[left+1:] = nums[left+1:][::-1]



sol = Solution()
nums=[1,2,3]
sol.nextPermutation(nums)
print nums
