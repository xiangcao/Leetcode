"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""

class Solution:
    # brute force
    def lengthOfLIS1(self, nums: List[int]) -> int:
        def helper(nums, prev, curpos):
            if curpos == len(nums):
                return 0
            lengthOfTaken = 0
            if prev == -1 or nums[curpos] > nums[prev]:
                lengthOfTaken = 1 + helper(nums, curpos, curpos+1)
            lengthNotTaken = helper(nums, prev, curpos+1)
            return max(lengthOfTaken, lengthNotTaken)
        return helper(nums, -1, 0)
  
    # DP O(n^2)
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [0] * (len(nums))
        dp[0] = 1
        for i, n in enumerate(nums):
            if i == 0:
                continue
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            dp[i] = max(dp[i], 1)
        return max(dp)
                
        
        

    # binary search O(nlogn)
    def lengthOfLIS3(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        length = 0
        for num in nums:
            i = bisect.bisect_left(dp, num, 0, length)
            dp[i] = num
            if i == length:
                length += 1
        return length

    """
    dp is an array such that dp[i] is the smallest element that ends an increasing subsequence of length i + 1. Whenever we encounter a new element e, we binary search inside dp to find the largest index i such that e can end that subsequence. We then update dp[i] with e.
    The length of the LIS is the same as the length of dp, as if dp has an index i, then it must have a subsequence of length i+1.
    """          
    # binary search NLogn 
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        for i in range(len(nums)):
            idx = bisect.bisect_left(dp, nums[i])
            if idx == len(dp):
                dp.append(nums[i])
            else:
                dp[idx] = nums[i]
        return len(dp) 
