class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [0 for i in nums]
        output[0] = nums[0]
        for i in range(1, len(nums)):
            output[i] = output[i-1] * nums[i]
        rightproduct = 1
        for i in reversed(range(1, len(nums))):
            output[i] = output[i-1] * rightproduct
            rightproduct *= nums[i]
        output[0] = rightproduct
        return output

nums =[0,8]

nums = [1,2,3]
