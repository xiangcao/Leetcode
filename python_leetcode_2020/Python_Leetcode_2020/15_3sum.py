class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        res=[]
        def twoSum(i):
            l, r = i+1, len(nums)-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
 
                if total > 0 or ((r < len(nums)-1) and nums[r] == nums[r+1]):
                    r -= 1
                elif total < 0 or (l > i+1 and nums[l] == nums[l-1]):
                    l += 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                twoSum(i)
        return res
