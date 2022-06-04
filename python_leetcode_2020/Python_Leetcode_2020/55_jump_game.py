"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.
"""

class Solution:
    # DP Bottom UP
    def canJump1(self, nums: List[int]) -> bool:
        reachable = [0] * len(nums)
        reachable[-1] = 1
        for i in reversed(range(len(nums)-1)):
            steps = nums[i]
            for k in range(steps):
                if i + k + 1 >= len(nums):
                    break
                if reachable[i+k+1] == 1:
                    reachable[i] = 1
                    break
        return reachable[0] 

"""
Once we have our code in the bottom-up state, we can make one final, important observation. From a given position, when we try to see if we can jump to a GOOD position, we only ever use one - the first one (see the break statement). In other words, the left-most one. If we keep track of this left-most GOOD position as a separate variable, we can avoid searching for it in the array. Not only that, but we can stop using the array altogether.
"""
    # Greedy
    def canJump(self, nums: List[int]) -> bool:
        leftMostGood = len(nums) - 1
        for i in reversed(range(len(nums)-1)):
            if (i + nums[i] >= leftMostGood):
                leftMostGood = i
        return leftMostGood == 0

    
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        # max position one could reach 
        # starting from index <= i
        max_pos = nums[0]
        
        for i in range(1, n):
            # if one could't reach this point
            if max_pos < i:
                return False
            max_pos = max(max_pos, nums[i] + i)

        return True
# Round 2
    # time limited
    # DP O(N^2)
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[0] = True
        for i in range(1, len(nums)):
            for j in range(i):
                if dp[j] and nums[j] + j >= i:
                    dp[i] = True
                    break
        return dp[-1]
    
    # Greedy  O(N)
    def canJump(self, nums: List[int]) -> bool:
        maxreach = nums[0]
        for i in range(1, len(nums)):
            if maxreach < i:
                return False
            maxreach = max(maxreach, nums[i] + i)
        return True
