#55. Jump Game
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxRight = 0 
        for i in range(len(nums)):
            if i > maxRight: return False
            maxRight = max(maxRight, i + nums[i])
        return True
                
