class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        if len(nums) == 0:
            return result
        left = nums[0]
        def getRange(left, right):
            if left == right:
                return str(left)
            elif left < right:
                return str(left)+"->"+str(right)

        for k in range(1, len(nums)+1):
            if k == len(nums):  # this condition was not handled well in my first try. consider this situation: [1,2], or [1] or [1,3]
                result.append(getRange(left, nums[k-1]))
                break
            if nums[k] - nums[k-1] > 1:
                result.append(getRange(left, nums[k-1]))
                left = nums[k]
        return result
        
