class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums.sort()
        result = None
        for i in range(len(nums)):
            l, r = i + 1, len(nums)-1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]

                if result is None or abs(sum-target) < abs(result - target):
                    result = sum
                if sum < target:
                    l += 1
                elif sum > target:
                    r -= 1
                else:
                    return sum
        return result
